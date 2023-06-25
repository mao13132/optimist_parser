from datetime import datetime

from browser.createbrowser import CreatBrowser
from src.source_parse import SourceParse


def main():
    filter_count_day = 1

    browser_core = CreatBrowser()

    print(f'Парсер запущен. Получаю данные')

    response_job = SourceParse(browser_core.driver, filter_count_day).start_pars()

    file_name = f'{datetime.now().strftime("%H_%M_%S")}'


if __name__ == '__main__':
    main()

    print(f'Работу закончил')
