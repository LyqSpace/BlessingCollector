import configparser
from os.path import dirname, abspath


def get_base_dir():
    BASE_DIR = dirname(dirname(abspath(__file__)))
    return BASE_DIR


def init():
    print('\nBlessing Collector Set Up Successfully !!!\n')


def database_config():
    BASE_DIR = get_base_dir()

    cp = configparser.ConfigParser()
    cp.read(BASE_DIR + '/utility/database.conf')

    host = cp.get('DATABASE', 'host')
    user = cp.get('DATABASE', 'user')
    password = cp.get('DATABASE', 'password')
    database = cp.get('DATABASE', 'database')

    return host, user, password, database