from django.template import loader
from utility import SqlEngine
from utility.functions import database_config


def add_birthday_unit():
    template = loader.get_template('web_event_management/add_birthday_unit.html')
    context = {}
    return template.render(context)


def add_event_unit():
    template = loader.get_template('web_event_management/add_event_unit.html')
    context = {}
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

        if row['USER2'] is not None:
            query_str = 'select FULLNAME from users where EMAIL=\'{0}\''.format(row['USER2'])
            sql_result = sql_engine.select_query(query_str)
            if len(sql_result) > 0:
                user += '<br>' + sql_result[0]['FULLNAME']

        if row['USER3'] is not None:
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

        query_str = 'insert events(DESCRIPTION, HAPPEN_DATE, USER1, TYPE) ' \
                    'values(\'生日祝福\', \'{0}\', \'{1}\', \'BIRTHDAY\')'.format(
                        bless_date,
                        row['EMAIL']
                    )
        try:
            sql_engine.execute_query(query_str)
        except Exception:
            return 'FAIL', '批量添加祝福事件失败！在 {0} 处'.format(row['FULLNAME'])

    return 'SUCCESS', ''
