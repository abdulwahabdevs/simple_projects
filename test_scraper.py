import time
import re
from typing import Final
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Regex used for finding emails in text
EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Regex used for finding phone numbers in text
NUMBER_REGEX: Final[str] = r"^(\+1|1)?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"

class Browser:
    def __init__(self, driver: str):
        print("Initializing Browser...")
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")


        self.browser = webdriver.Chrome(options=self.chrome_options)

    # mail scraper
    def scrape_emails(self, url: str) -> set:
        print(f"Scraping '{url}' for emails...")
        self.browser.get(url)
        page_source = self.browser.page_source

        list_of_emails: set = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())

        return list_of_emails

    # Phone number scraper
    def scrape_number(self, url: str) -> set:
        print(f"Scraping '{url}' for phone numbers...")
        self.browser.get(url)
        page_source = self.browser.page_source

        list_of_numbers: set = set()
        for re_match in re.finditer(NUMBER_REGEX, page_source):
            list_of_numbers.add(re_match.group())

        return list_of_numbers

    def close_page(self):
        print(f'Closing browser...')
        self.browser.close()

def main():
    driver: str = 'chromedriver'
    browser = Browser(driver=driver)

    emails: set = browser.scrape_emails(url='https://www.python.org')
    if emails:
        for i, email in enumerate(emails, start=1):
            print(i, email, sep=': ')
    else:
        print('No emails found.')
    # numbers: set = browser.scrape_number(url='https://www.randomlists.com/phone-numbers#google_vignette')
    # if numbers:
    #     for i, number in enumerate(numbers, start=1):
    #         print(i, number, sep=': ')
    # else:
    #     print('No numbers found.')

if __name__ == '__main__':
    main()
