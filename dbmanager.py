import psycopg2
from config import config


class DBManager:

    def __init__(self, db_name: str):
        self.db_name = db_name

    def get_companies_and_vacancies_count(self):
        params = config()
        conn = psycopg2.connect(dbname=self.db_name, **params)

        with conn.cursor() as cur:
            # cur.execute("""
            # SELECT * FROM company
            # """)
            # list_company = []
            # list_vacancies = []
            # rows = cur.fetchall()
            # for row in rows:
            #     list_company.append(row)

            # for i in range(len(list_company)):
            cur.execute(f"""
            SELECT company_name, company_id FROM vacancies
            """)
            rows_1 = cur.fetchall()
            count1 = 0
            for i in rows_1:
                if i[1] == 1:
                    count1 += 1
            # list_vacancies.append(rows_1)

            # cur.execute("""
            #             SELECT COUNT(*) FROM vacancies
            #             WHERE company_id = 2
            #             """)
            # rows_2 = cur.fetchall()

        conn.commit()
        conn.close()
        # print(rows_1)
        # info_dict = {list_company[0][1]: list_vacancies[0][0][0], list_company[1][1]: list_vacancies[1][0][0],
        #              list_company[2][1]: list_vacancies[2][0][0]}

        return rows_1

    # def get_all_vacancies(self):
    #     params = config()
    #     conn = psycopg2.connect(dbname=self.db_name, **params)
    #
    #     with conn.cursor() as cur:
    #         cur.execute("""
    #         SELECT * FROM company
    #         """)
    #         list_company = []
    #         rows = cur.fetchall()
    #         for row in rows:
    #             list_company.append(row)
    #
    #         cur.execute("""
    #         SELECT * FROM vacancies
    #         WHERE company_id = 1
    #         """)
    #         rows_1 = cur.fetchall()
    #
    #         cur.execute("""
    #                     SELECT * FROM vacancies
    #                     WHERE company_id = 2
    #                     """)
    #         rows_2 = cur.fetchall()
    #
    #     conn.commit()
    #     conn.close()

    # info_list =
