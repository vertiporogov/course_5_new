import psycopg2
from config import config


class DBManager:

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:

            cur.execute(f"""
            SELECT DISTINCT company_name FROM vacancies
            """)
            rows_1 = cur.fetchall()

        conn.commit()
        conn.close()

        return rows_1

    # def get_all_vacancies(self):
    #     params = config()
    #     conn = psycopg2.connect(dbname=self.db_name, **params)
    #
    #     with conn.cursor() as cur:
