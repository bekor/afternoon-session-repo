import psycopg2
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))

private_connection = SourceFileLoader("private_connection", current_file_path + "/private_connection.py").load_module()


def connection(func):
    def connection_wrapper():
        try:
            # setup connection string
            connect_str = private_connection.private_config()

            # use our connection values to establish a connection
            connection = psycopg2.connect(host=connect_str["host"],
                                          user=connect_str["user"],
                                          dbname=connect_str["dbname"],
                                          password=connect_str["password"]
                                          )

            # set autocommit option, to do every query when we call it
            connection.autocommit = True

            # create a psycopg2 (client side) cursor that can execute queries
            cursor = connection.cursor()

            sql_query_func = func(cursor)

            # Close communication with the database
            cursor.close()

        # This exception may not be enough.
        except psycopg2.DatabaseError as exception:
            print(exception)
            # If you want to handle it on an other level:
            # raise DatabaseError("Error in connnection: %s" % (exception))
            # finally block will run no matter what

        finally:
            if connection:
                connection.close()
        return sql_query_func
    return connection
