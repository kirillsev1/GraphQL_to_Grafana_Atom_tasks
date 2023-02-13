from manage_db import init_database, fill_db
from logger import init_logger
import requests
import logging
import json

logger = logging.getLogger('app.main.file')
URL = 'https://spacex-production.up.railway.app/'
BODY = """
{
launches {
    mission_name
    rocket {
      rocket_name
      rocket_type
    }
    launch_date_local
  }
}
"""


def collect_data(url=URL, body=BODY):
    """Function which sends request to GraphQL.

    Args:
        url: str - url on sandbox in  GraphQL.
        body: str - body of request on GraphQL.

    Returns:
        str - answer on request.
    """
    logger.info('Start collect_data function')
    response = requests.post(url=url, json={'query': body})
    logger.info('Request was sent')
    logger.info('Response code: {0}'.format(response.status_code))
    if response.status_code == 200:
        json_data = json.loads(response.content)
        df_data = json_data['data']['launches']
        logger.info('Start filling database')
        for data in df_data:
            fill_db(data)
        logger.info('Database was filled')
    logger.info('Function collect_data finished')


def main():
    """Main function which call initialises function and data collection function."""
    init_logger('app')
    init_database()
    collect_data()


if __name__ == '__main__':
    main()
