import psycopg2

class db_manager:
    def __init__(self):
        self.__connection = None

    def connect(self):
        if not self.__connection or self.connection.closed:
            try:
                self.__connection = psycopg2.connect(
                    dbname="kr2",
                    user="postgres",
                    password="",
                    host="localhost",
                    port="5432"
                )
            except psycopg2.Error as e:
                print(f"database connection error: {e}")
                raise
            return self
        
    def close(self):
        if self.__connection and not self.__connection.closed:
            self.__connection.close()
        return self
    
    def get_all_employees(self) -> list:
        cur = self.__connection.cursor()
        cur.execute("""
        SELECT *
        FROM employees;
        """)

        yemployees = cur.fetchall()
        cur.close()

        return yemployees