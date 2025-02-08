from typing import Final
import requests
import config

API_KEY: Final[str] = config.api_key
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_url(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link: ', short_link)
        else:
            print('Something went wrong!', url_data['status'])

def main():
    url_input: str = input('Enter the url to shorten: ')
    shorten_url(url_input)

if __name__ == '__main__':
    main()


