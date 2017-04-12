from django.template import loader
from utility import SqlEngine
from utility.functions import database_config


def new_user_unit():
    template = loader.get_template('web_user_management/new_user_unit.html')
    context = {
    }
    return template.render(context)


def update_old_user_unit():
    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'select EMAIL, FULLNAME from users'
    sql_result = sql_engine.select_query(query_str)

    user_list = []
    for row in sql_result:
        user = {
            'EMAIL': row['EMAIL'],
            'FULLNAME': row['FULLNAME']
        }
        user_list.append(user)

    template = loader.get_template('web_user_management/update_old_user_unit.html')
    context = {
        'user_list': user_list
    }
    return template.render(context)


def create_new_user(request):

    sql_engine = SqlEngine.SqlEngine(database_config)

    try:
        query_str = 'insert into USERS(EMAIL, FULLNAME, BIRTHDAY) ' \
                    'values(\'{0}\', \'{1}\', \'{2}\')'.format(
            request.POST['email'],
            request.POST['fullname'],
            request.POST["birthday"],
        )
    except KeyError:
        return 'FAIL', '新建用户参数缺失！'

    temp_sql = 'select * from users where EMAIL=\'{0}\''.format(request.POST['email'])
    sql_result = sql_engine.select_query(temp_sql)
    if len(sql_result) > 0:
        return 'FAIL', '用户的邮箱已存在！'

    try:
        sql_engine.execute_query(query_str)
    except Exception:
        return 'FAIL', '数据库插入数据失败！'

    return 'SUCCESS', ''


def select_old_user(request):

    try:
        email = request.GET['email']
    except KeyError:
        return 'FAIL', '查询用户参数缺失！', ''

    sql_engine = SqlEngine.SqlEngine(database_config)

    # 获取用户信息
    query_str = 'select * from users where EMAIL=\'{0}\''.format(email)
    sql_result = sql_engine.select_query(query_str)

    if len(sql_result) == 0:
        return 'FAIL', '查找不到相应用户！', ''

    user_basic_info = {
        'EMAIL': sql_result[0]['EMAIL'],
        'FULLNAME': sql_result[0]['FULLNAME'],
        'BIRTHDAY': str(sql_result[0]['BIRTHDAY']),
    }

    # 渲染网页
    template = loader.get_template('web_user_management/user_profile.html')
    context = {
        'user': user_basic_info,
    }

    return 'SUCCESS', None, template.render(context)


def update_user_info(request):

    try:
        field = request.POST['field']
        value = request.POST['value']
        email = request.POST['email']
    except KeyError:
        return 'FAIL', '更新用户信息参数缺失！'

    sql_engine = SqlEngine.SqlEngine(database_config)
    sql_engine.connect()

    query_str = 'update users set {0}=\'{1}\' where EMAIL=\'{2}\''.format(
        field,
        value,
        email
    )

    try:
        sql_engine.execute_query(query_str)
    except Exception:
        return 'FAIL', '插入数据库失败！'

    return 'SUCCESS', '更新用户信息成功！'
