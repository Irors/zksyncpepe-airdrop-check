from sdk.addLogger import add_logger
from sdk.zksyncpepe import main_check
from loguru import logger

with open('Data/wallets.txt') as apw:
    wallets = [row.strip() for row in apw]


if __name__ == '__main__':
    add_logger()

    logger.info('Начинаю парсить')
    main_check(wallets)

    logger.success('Закончил парсить успешно')