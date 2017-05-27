import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

sql_connection = SourceFileLoader("sql_connection", current_file_path + "/server_connection/sql_connection.py").load_module()


# If you import only the .py file not a function you have to use the following form of the decorator func.
@sql_connection.connection
def select_applicants(cursor):
    query = """SELECT * FROM applicant;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
    # except psycopg2.ProgrammingError as er:
    #     print("Here is the query error: %s" % er)


if __name__ == '__main__':
    dew = select_applicants()
    print(dew)


