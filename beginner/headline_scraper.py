from bs4 import BeautifulSoup
import requests

def get_soup()->BeautifulSoup:
    headers: dict = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'
    }

    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes = request.content

    # Create soup
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup)->list[str]:
    headlines: set = set()

    for h in soup.find_all('h2', class_='sc-8ea7699c-3'):
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return headlines

def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    term_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if (' ' + term.lower() + ' ') in (' ' + headline + ' '):
            term_found += 1
            term_list.append(headline)
            print(f'{i}. {headline.capitalize()} <-----------------------> {term}')
        else:
            print(f'{i}. {headline.capitalize()}')

    # Divider
    print('----------------------------------------------')
    if term_found:
        print(f'{term} was mentioned {term_found} times.')
        # Divider
        print('----------------------------------------------')

        for i, headline in enumerate(term_list, start=1):
            print(f'{i}. {headline.capitalize()}')
    else:
        print(f'Nothing was found: {term}')
        # Divider
        print('----------------------------------------------')


def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    user_input: str = input('Enter headline: ')
    check_headlines(headlines, user_input)


if __name__ == '__main__':
    main()


