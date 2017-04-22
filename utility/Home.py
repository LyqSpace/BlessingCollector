from django.template import loader
from utility import SqlEngine
from utility.functions import database_config


def event_list_unit(request):

    try:
        email = request.COOKIES['email']
    except KeyError:
        return 'FAIL', '缺少用户参数！'

    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'select * from events where USER1 != \'{0}\' and USER2 != \'{0}\' and USER3 != \'{0}\''.format(email)
    sql_result = sql_engine.select_query(query_str)

    event_list = []
    for row in sql_result:
        event_info = {
            'ID': row['ID'],
            'HAPPEN_DATE': str(row['HAPPEN_DATE']),
            'DESCRIPTION': row['DESCRIPTION'],
        }

        query_str = 'select * from users where EMAIL=\'{0}\''.format(row['USER1'])
        user_result = sql_engine.select_query(query_str)
        user = user_result[0]['FULLNAME']

        if row['USER2'] != 'NULL':
            query_str = 'select * from users where EMAIL=\'{0}\''.format(row['USER2'])
            user_result = sql_engine.select_query(query_str)
            user += '<br>' + user_result[0]['FULLNAME']

        if row['USER3'] != 'NULL':
            query_str = 'select * from users where EMAIL=\'{0}\''.format(row['USER3'])
            user_result = sql_engine.select_query(query_str)
            user += '<br>' + user_result[0]['FULLNAME']

        event_info['USER'] = user

        query_str = 'select * from event_blessings where EVENT_ID=\'{0}\' and EMAIL=\'{1}\''.format(
            row['ID'], email
        )
        blessing_result = sql_engine.select_query(query_str)

        try:
            event_info['BLESSING'] = blessing_result[0]['MESSAGE']
        except IndexError:
            event_info['BLESSING'] = ''

        event_list.append(event_info)

    if len(event_list) == 0:
        return '暂无祝福事件'
    else:
        template = loader.get_template('web_home/event_list_unit.html')
        context = {
            'event_list': event_list
        }

        return template.render(context)


def save_blessing(request):
    try:
        email = request.COOKIES['email']
        blessing = request.POST['BLESSING']
        event_id = request.POST['EVENT_ID']
    except KeyError:
        return 'FAIL', '保存祝福缺少参数！'

    sql_engine = SqlEngine.SqlEngine(database_config)
    query_str = 'delete from event_blessings where EVENT_ID=\'{0}\' and EMAIL=\'{1}\''.format(
        event_id, email
    )
    try:
        sql_engine.execute_query(query_str)
    except Exception:
        return 'FAIL', '保存祝福失败！'

    query_str = 'insert into event_blessings(EVENT_ID, EMAIL, MESSAGE) ' \
                'values(\'{0}\', \'{1}\', \'{2}\')'.format(
        event_id, email, blessing
    )
    try:
        sql_engine.execute_query(query_str)
    except Exception:
        return 'FAIL', '保存祝福失败！'

    return 'SUCCESS', '保存祝福成功！'
