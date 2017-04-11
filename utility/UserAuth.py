from utility import SqlEngine
from utility.functions import database_config


class UserAuth:

    def __init__(self):
        self._sql_engine = SqlEngine.SqlEngine(database_config)

    def login(self, email, token):

        query_str = 'select * from login_token where TOKEN=\'{0}\''.format(token)

        sql_result = self._sql_engine.select_query(query_str)

        if len(sql_result) == 0:
            return 'AUTH_FAIL', '口令错误！', ''

        query_str = 'select FULLNAME from users where EMAIL=\'{0}\''.format(email)

        sql_result = self._sql_engine.select_query(query_str)

        if len(sql_result) == 0:
            return 'AUTH_FAIL', '邮箱不存在！', ''

        fullname = sql_result[0]['FULLNAME']

        return 'SUCCESS', '登录成功！', fullname

    def user_auth(self, cookies, module=None):

        email = cookies.get('email')
        token = cookies.get('token')

        if email is None or token is None:
            return False

        state, message, fullname = self.login(email, token)

        if state != 'SUCCESS':
            return False

        if module == 'SUPER_ADMIN':
            if email == 'root@lyq.me':
                return True
            else:
                return False
        else:
            return True
