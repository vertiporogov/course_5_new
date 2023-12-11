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
            SELECT DISTINCT company_name FROM companies
            """)
            rows_1 = cur.fetchall()

            cur.execute(f"""
                        SELECT COUNT(*) FROM vacancies
                        WHERE company_id = 1
                        """)
            count_1 = cur.fetchall()

            cur.execute(f"""
                                    SELECT COUNT(*) FROM vacancies
                                    WHERE company_id = 2
                                    """)
            count_2 = cur.fetchall()

            cur.execute(f"""
                                    SELECT COUNT(*) FROM vacancies
                                    WHERE company_id = 3
                                    """)
            count_3 = cur.fetchall()

        conn.commit()
        conn.close()

        result = {rows_1[0][0]: count_1[0][0], rows_1[1][0]: count_2[0][0], rows_1[2][0]: count_3[0][0]}

        return result

    # def get_all_vacancies(self):
    #     params = config()
    #     conn = psycopg2.connect(dbname=self.db_name, **params)
    #
    #     with conn.cursor() as cur:
