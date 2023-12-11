from utils import get_info_company, create_database, create_table, save_date_to_table
from config import config
from dbmanager import DBManager

company_id = [
    1740,  # Яндекс
    1221656,  # НЭМО
    1040211  # elama
]


def main():
    params = config()

    data_company = []

    for i in company_id:
        data = get_info_company(i)
        data_company.append(data)

    create_database('headhunterparser', params)   # Создаем базу данных
    create_table('headhunterparser', params)    # Создаем таблицы
    save_date_to_table(data_company, 'headhunterparser', params)    # Заполняем таблицы нашими данными

    # Создаем экземпляр класса DBManager и вызываем все методы
    ff = DBManager('headhunterparser')
    print(ff.get_companies_and_vacancies_count())
    print(ff.get_all_vacancies())
    print(ff.get_avg_salary(2))
    print(ff.get_vacancies_with_higher_salary(2))
    print(ff.get_vacancies_with_keyword('судовой'))


if __name__ == '__main__':
    main()
