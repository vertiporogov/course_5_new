from utils import get_info_company, get_info_vacancy, h, create_database, create_table, save_date_to_table
from config import config
from dbmanager import DBManager

company_id = [
    1740,  # Булочные Ф. Вольчека
    1221656,
    1040211# НЭМО
]


def main():
    params = config()

    data_company = []

    # for i in company_id:
    #     data = get_info_company(i)
    #     data_company.append(data)

    # create_database('headhunterparser', params)
    # create_table('headhunterparser', params)
    # save_date_to_table(data_company, 'headhunterparser', params)
    #
    ff = DBManager('headhunterparser')
    print(ff.get_companies_and_vacancies_count())
    print(ff.get_all_vacancies())
    print(ff.get_avg_salary(2))


    # for i in get_info_vacancy('https://api.hh.ru/vacancies?employer_id=2104700'):
    #     print(i)
    #     print('*' * 100)

    # print(get_info_vacancy('https://api.hh.ru/vacancies?employer_id=1740'))

    # print(h('https://api.hh.ru/vacancies?employer_id=1221656')['items'][0])
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
    # print(get_info_company('1221656'))
    # for i in get_info_company('1740'):
    #     print(i)
    #     print('*' * 100)


if __name__ == '__main__':
    main()
