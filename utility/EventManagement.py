from django.template import loader
from utility import SqlEngine
from utility.functions import database_config


def add_birthday_unit():
    template = loader.get_template('web_event_management/add_birthday_unit.html')
    context = {}
    return template.render(context)


def add_event_unit():
    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'select * from users where EMAIL != \'admin@bless\''
    user_result = sql_engine.select_query(query_str)

    default_option = {
        'EMAIL': 'NULL',
        'FULLNAME': '选择相关用户'
    }
    user_result.insert(0, default_option)

    template = loader.get_template('web_event_management/add_event_unit.html')
    context = {
        'user_list': user_result
    }
    return template.render(context)


def event_list_unit():
    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'select * from events order by HAPPEN_DATE desc'
    event_result = sql_engine.select_query(query_str)

    event_list = []
    for row in event_result:

        query_str = 'select FULLNAME from users where EMAIL=\'{0}\''.format(row['USER1'])
        sql_result = sql_engine.select_query(query_str)
        if len(sql_result) > 0:
            user = sql_result[0]['FULLNAME']

        if row['USER2'] != 'NULL':
            query_str = 'select FULLNAME from users where EMAIL=\'{0}\''.format(row['USER2'])
            sql_result = sql_engine.select_query(query_str)
            if len(sql_result) > 0:
                user += '<br>' + sql_result[0]['FULLNAME']

        if row['USER3'] != 'NULL':
            query_str = 'select FULLNAME from users where EMAIL=\'{0}\''.format(row['USER3'])
            sql_result = sql_engine.select_query(query_str)
            if len(sql_result) > 0:
                user += '<br>' + sql_result[0]['FULLNAME']

        event_info = {
            'HAPPEN_DATE': str(row['HAPPEN_DATE']),
            'DESCRIPTION': row['DESCRIPTION'],
            'USER': user,
        }

        event_list.append(event_info)

    template = loader.get_template('web_event_management/event_list_unit.html')
    context = {
        'event_list': event_list
    }
    return template.render(context)


def add_birthday(request):
    try:
        year = request.POST['year']
    except KeyError:
        return 'FAIL', '缺少年份参数！', ''

    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'select * from users where BIRTHDAY is not NULL'
    user_result = sql_engine.select_query(query_str)

    for row in user_result:

        birthday_list = str(row['BIRTHDAY']).split('-')
        bless_date = year + '-' + birthday_list[1] + '-' + birthday_list[2]
        query_str = 'select * from events where HAPPEN_DATE=\'{0}\' and USER1=\'{1}\' and events.TYPE="BIRTHDAY"'.format(
            bless_date, row['EMAIL']
        )

        sql_result = sql_engine.select_query(query_str)
        if len(sql_result) > 0:
            continue

        query_str = 'insert events(DESCRIPTION, HAPPEN_DATE, USER1, USER2, USER3, TYPE) ' \
                    'values(\'生日祝福\', \'{0}\', \'{1}\', \'NULL\', \'NULL\', \'BIRTHDAY\')'.format(
                        bless_date,
                        row['EMAIL']
                    )
        try:
            sql_engine.execute_query(query_str)
        except Exception:
            return 'FAIL', '批量添加祝福事件失败！在 {0} 处'.format(row['FULLNAME'])

    return 'SUCCESS', ''


def add_event(request):
    try:
        description = request.POST['DESCRIPTION']
        happen_date = request.POST['HAPPEN_DATE']
        user1 = request.POST['USER1']
        user2 = request.POST['USER2']
        user3 = request.POST['USER3']
    except KeyError:
        return 'FAIL', '缺少祝福事件参数！', ''

    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'insert events(DESCRIPTION, HAPPEN_DATE, TYPE, USER1, USER2, USER3) ' \
                'values(\'{0}\', \'{1}\', \'OTHERS\', \'{2}\', \'{3}\', \'{4}\')'.format(
        description, happen_date, user1, user2, user3
    )

    try:
        sql_engine.execute_query(query_str)
    except:
        return 'FAIL', '批量单个祝福事件失败！'

    return 'SUCCESS', ''
