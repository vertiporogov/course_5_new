import psycopg2
from config import config


class DBManager:
    """Класс для работы с базой данных"""

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
                SELECT companies.company_name, COUNT(vacancies.vacancy_id)
                FROM companies
                JOIN vacancies ON companies.company_id = vacancies.company_id
                GROUP BY companies.company_name;
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию."""
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
            SELECT vacancy_id, company_name, vacancy_name, salary, vacancy_url FROM vacancies
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    def get_avg_salary(self, company_id):
        """Получает среднюю зарплату по вакансиям."""
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT avg(salary) FROM vacancies
            WHERE company_id = {company_id}
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    def get_vacancies_with_higher_salary(self, company_id):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT * FROM vacancies
            WHERE company_id = {company_id} AND salary > (SELECT AVG(salary) FROM vacancies)
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result

    def get_vacancies_with_keyword(self, word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT * FROM vacancies
            WHERE vacancy_name LIKE '%{word}%'
            """)

            result = cur.fetchall()

        conn.commit()
        conn.close()

        return result
