import psycopg2
from config import config


class DBManager:

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):

        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM company
            """)
            list_company = []
            rows = cur.fetchall()
            # print(type(rows))
            for row in rows:
                list_company.append(row)

            cur.execute("""
            SELECT COUNT(*) FROM vacancies
            WHERE company_id = 2
            """)
            rows_ = cur.fetchall()
            # count_1 = 0
            # count_2 = 0
            # for row in rows_:
            #     if row[1] == 1:
            #         count_1 += 1
            #     else:
            #         count_2 += 1

        conn.commit()
        conn.close()

        # print(f'{list_company[0][1]} имеет вакансий {count_1}')
        # print(f'{list_company[1][1]} имеет вакансий {count_2}')
        print(rows_[0][0])