import logging
import psycopg2
import os


DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
logger = logging.getLogger('app.manage_db.file')


def fill_db(data, database=DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT):
    """Function which fills database line by line.

    Args:
        data: str - dict of values from GraphQL.
        database: str - name of database.
        user: str - name of database user.
        password: str - users password.
        host: str - host for database.
        port: str - port on which database works.
    """

    with psycopg2.connect(database=database, user=user, password=password, host=host, port=port) as con:
        cur = con.cursor()
        rocket = data['rocket']

        cur.execute('INSERT INTO missions (name) VALUES (%s) RETURNING id', (data['mission_name'],))
        mission_id = cur.fetchone()[0]

        cur.execute('SELECT id FROM rockets WHERE name = %s;', (rocket['rocket_name'],))
        rocket_id = cur.fetchone()
        print('Rocket_id: {0}, Mission_id: {1}'.format(rocket_id, mission_id))

        if not rocket_id:
            cur.execute('INSERT INTO rockets (name, type) VALUES (%s, %s) RETURNING id',
                        (rocket['rocket_name'], rocket['rocket_type']))
            rocket_id = cur.fetchone()

        rocket_id = rocket_id[0]
        cur.execute('INSERT INTO launches (mission_id, rocket_id, launch_date_local) VALUES (%s, %s, %s)',
                    (mission_id, rocket_id, data['launch_date_local']))


def init_database(database=DATABASE, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT):
    """Function which initialises tables in database.

    Args:
        database: str - name of database.
        user: str - name of database user.
        password: str - users password.
        host: str - host for database.
        port: str - port on which database works.
    """
    logger.info('Start init_database function')
    logger.info('Connecting to postgres')
    with psycopg2.connect(database=database, user=user, password=password, host=host, port=port) as con:
        cur = con.cursor()
        with open('init_table.sql', 'r') as file:
            cur.execute(file.read())
            logger.info('Tables were created')
    logger.info('Function init_database finished')
