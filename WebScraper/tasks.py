import os
os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "proj.settings"

from celery import task
from bs4 import BeautifulSoup
import logging
import requests
import redis
import time
from celery import shared_task


logger = logging.getLogger(__name__)

@shared_task
def get_table_data(url):
    logger.info('Starting')
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(url, 'html.parser')
        table = soup.find('table')
        if table:
            table_data = []
            for row in table.find_all('tr'):
                row_data = [cell.get_text() for cell in row.find_all(['th', 'td'])]
                table_data.append(row_data)
            return table_data
        else:
            raise ValueError("No table found on the webpage.")
    else:
        raise ValueError(f"Failed to fetch webpage. Status code: {response.status_code}")