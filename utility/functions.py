import configparser


def init():
    print('\nBlessing Collector Set Up Successfully !!!\n')


def database_config():
    cp = configparser.ConfigParser()
    cp.read('utility/database.conf')

    host = cp.get('DATABASE', 'host')
    user = cp.get('DATABASE', 'user')
    password = cp.get('DATABASE', 'password')
    database = cp.get('DATABASE', 'database')

    return host, user, password, database