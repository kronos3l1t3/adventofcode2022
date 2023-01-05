import requests
from bs4 import BeautifulSoup


cookies = {
    '_ga': 'GA1.2.632825991.1648359887',
    '_gid': 'GA1.2.1219079471.1648359887',
    'session': '53616c7465645f5f20da67e563940ef2c5e9b4d37bc530d0a8b2e9dbaf7df95a336d6b38dee9ce3197fbc2c37d86c1352d31424abf62ee6478ecaae8585c7979',
}

headers = {
    'authority': 'adventofcode.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://adventofcode.com/2017/day/6',
    'accept-language': 'es-ES,es;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.632825991.1648359887; _gid=GA1.2.1219079471.1648359887; session=53616c7465645f5f20da67e563940ef2c5e9b4d37bc530d0a8b2e9dbaf7df95a336d6b38dee9ce3197fbc2c37d86c1352d31424abf62ee6478ecaae8585c7979',
}


def extract_data(day):
    response = requests.get('https://adventofcode.com/2021/day/'+str(day)+'/input', headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify().strip().split('\n')
