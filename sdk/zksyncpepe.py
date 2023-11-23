import asyncio
from loguru import logger
import aiohttp
from sdk.excel import Excel

async def get_response(response):
    return await response.content.read()

async def reqst(address: str, number: int):

    async with aiohttp.ClientSession() as session:
        try:
            response = await session.get(f'https://www.zksyncpepe.com/resources/amounts/{address.lower()}.json')
            token = await get_response(response)

            Excel.sheet[f'A{number+1}'] = address
            if len(token.decode()[1:-1]) < 10:
                Excel.sheet[f'B{number+1}'] = int(token.decode()[1:-1])
            else:
                Excel.sheet[f'B{number+1}'] = 0

        except Exception as e:
            logger.error(f'Ошибка: {e}')

async def get_eligible(wallets: list):

    tasks = []
    logger.info(f'Найдено {len(wallets)} кошельков')
    for address in wallets:
        tasks.append(asyncio.create_task(reqst(address, wallets.index(address)+1)))

    await asyncio.gather(*tasks)

def main_check(wallets: list):
    Excel()

    #try:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_eligible(wallets))
    loop.close()

    #except:
    #    logger.error('Проблема с указанием кошелька(ов)')


    Excel.workbook.save('results/result.xlsx')