from utils import get_info_company, get_info_vacancy, h, create_database, create_table, save_date_to_table
from config import config
from dbmanager import DBManager

company_id = [
    1413874,  # Булочные Ф. Вольчека
    1221656,  # НЭМО
]


def main():
    params = config()

    data_company = []

    for i in company_id:
        data = get_info_company(i)
        data_company.append(data)

    create_database('headhunterparser', params)
    create_table('headhunterparser', params)
    save_date_to_table(data_company, 'headhunterparser', params)

    ff = DBManager('headhunterparser')
    ff.get_companies_and_vacancies_count()


    # for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=2104700')['items']:
    #     print(i)
    #     print('*' * 100)

    # print(get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1740'))

    # print(h('https://api.hh.ru/vacancies?employer_id=1740'))
    # for i in h('https://api.hh.ru/vacancies?employer_id=1740')['items']:
    #     print(i)
    #     print(' ')
    #     print('*' * 100)
    #     print(' ')

    # for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1413874'):
    #     print(i)
    #     print(' ')
    #     print('*' * 100)
    #     print(' ')
    # print(get_info_company('1740'))
    # for i in get_info_company('1740'):
    #     print(i)
    #     print('*' * 100)


if __name__ == '__main__':
    main()
