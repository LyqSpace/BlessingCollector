import pymysql


class SqlEngine:
    def __init__(self, database_config):
        self._host, self._user, self._password, self._database = database_config()
        self._conn = None
        self._cur = None

        self.connect()

        # DEBUG
        # print(self._host, self._user, self._password, self._database)

    def __del__(self):
        self._close()

    def connect(self):
        self._conn = pymysql.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database,
            port=3306,
            charset="utf8")

        self._cur = self._conn.cursor(pymysql.cursors.DictCursor)

    def select_query(self, sql_str):
        try:
            self._cur.execute(sql_str)
            result = self._cur.fetchall()
            if len(result) == 0:
                return []
            else:
                return result
        except Exception as e:
            print(e)
            return []

    def execute_query(self, sql_str):
        self._cur.execute(sql_str)
        self._conn.commit()

    def _close(self):
        self._cur.close()
        self._conn.close()

    @property
    def conn(self):
        return self._conn

    def init_database(self):
        print("Initialize Database")

        sql_file = open('init_database.sql', 'r')
        query_str = sql_file.read()
        self.execute_query(query_str)