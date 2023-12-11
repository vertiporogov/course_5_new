from typing import Any

import psycopg2
from requests import get
import json


def get_info_company(id_company: str) -> dict[str, Any]:
    """Возвращает данные о канале по id канала"""
    hh_api = f"https://api.hh.ru/employers/{id_company}"
    response = get(hh_api)
    company = json.loads(response.content.decode())
    company_dict = {
        'company_id': company['id'],
        'company_name': company['name'],
        'company_url': company['alternate_url'],
        'vacancies_url': company['vacancies_url']
    }

    return company_dict


def h(dd):
    """Функция хэлпер"""
    hh_api = dd
    response = get(hh_api)
    vacancy = json.loads(response.content.decode())
    return vacancy


def get_info_vacancy(vacancy_url: str) -> list[dict[str, Any]]:
    """Возвращает список словарей с данными о вакансиях"""
    vacancy_list = []

    hh_api = vacancy_url
    response = get(hh_api)
    vacancy = json.loads(response.content.decode())

    for i in vacancy['items']:

        if i['salary'] is None:
            vacancy_dict = {
                'vacancy_id': i['id'],
                'company_name': i['employer']['name'],
                'vacancy_name': i['name'],
                'vacancy_url': i['employer']['alternate_url'],
                'salary': 0,
                'area': i['area']['name']
            }
            vacancy_list.append(vacancy_dict)

        else:
            if i['salary']['from'] is None:
                vacancy_dict = {
                    'vacancy_id': i['id'],
                    'company_name': i['employer']['name'],
                    'vacancy_name': i['name'],
                    'vacancy_url': i['employer']['alternate_url'],
                    'salary': 0,
                    'area': i['area']['name']
                }
                vacancy_list.append(vacancy_dict)

            else:
                if i['salary']['currency'] == 'RUR':
                    vacancy_dict = {
                        'vacancy_id': i['id'],
                        'company_name': i['employer']['name'],
                        'vacancy_name': i['name'],
                        'vacancy_url': i['employer']['alternate_url'],
                        'salary': i['salary']['from'],
                        'area': i['area']['name']
                    }
                    vacancy_list.append(vacancy_dict)

    return vacancy_list


def create_database(database_name: str, params) -> None:
    """Создаёт базу данных"""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()


def create_table(database_name: str, params) -> None:
    """Создаёт таблицы в базе данных"""
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE companies (
        company_id serial PRIMARY KEY,
        company_name varchar(100) NOT NULL,
        company_id_to_hh int,
        company_URL text,
        vacancies_url text
        )
        """)

    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE vacancies (
        vacancy_id serial PRIMARY KEY,
        company_id int REFERENCES companies(company_id),
        company_name varchar(100) NOT NULL,
        vacancy_name varchar(100),
        vacancy_url text,
        salary int,
        area varchar(100)
        )
        """)

    conn.commit()
    conn.close()


def save_date_to_table(data_company: list[dict[str, Any]], database_name: str, params) -> None:
    """Заполняет таблицы данными"""
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for i in data_company:
            cur.execute("""
            INSERT INTO companies (company_name, company_id_to_hh, company_URL, vacancies_url)
            VALUES (%s, %s, %s, %s)
            RETURNING company_id
            """,
                        (i['company_name'], i['company_id'], i['company_url'], i['vacancies_url']))

            company_id = cur.fetchone()[0]

            list_vacancies_dict = get_info_vacancy(i['vacancies_url'])

            for ii in list_vacancies_dict:
                cur.execute("""
                                        INSERT INTO vacancies (company_id, company_name, vacancy_name, vacancy_url,
                                         salary, area)
                                        VALUES (%s, %s, %s, %s, %s, %s)
                                        """,
                            (
                                company_id, ii['company_name'], ii['vacancy_name'], ii['vacancy_url'], ii['salary'],
                                ii['area']))

    conn.commit()
    conn.close()
