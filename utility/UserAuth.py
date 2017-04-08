from utility import SqlEngine
from utility.functions import database_config


class UserAuth:

    def __init__(self):
        self._sql_engine = SqlEngine.SqlEngine(database_config)

    def login(self, email, password):

        query_str = 'select * from bless_password where PASSWORD=\'{0}\''.format(password)

        sql_result = self._sql_engine.select_query(query_str)

        if len(sql_result) == 0:
            return 'AUTH_FAIL', '口令错误', ''

        query_str = 'select FULLNAME from bless_users where EMAIL=\'{0}\''.format(email)

        sql_result = self._sql_engine.select_query(query_str)

        if len(sql_result) == 0:
            return 'AUTH_FAIL', '邮箱不存在', ''

        fullname = sql_result[0]['FULLNAME']

        return 'SUCCESS', '登录成功', fullname

    def user_auth(self, cookies, module=None):

        email = cookies.get('email')
        password = cookies.get('password')

        if email is None or password is None:
            return False

        state = self.login(email, password)

        if state != 'SUCCESS':
            return False

        if module == 'SUPER_ADMIN':
            if email == 'root@lyq.me':
                return True
            else:
                return False
        else:
            return True
