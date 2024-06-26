import os
import requests
from retry import retry
from requests.exceptions import Timeout

api_url = os.getenv('BR_API_URL')


@retry(Timeout)
def get_stock_info(stock: str) -> dict:
    try:
        response = requests.get(api_url.format(stock))

        return response.json()
    except Timeout as e:
        raise e
    except Exception as e:
        print('Request API Error: ', str(e))
