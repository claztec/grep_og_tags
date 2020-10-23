import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from spider.exception import CrawlingError


def __load_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')

    try:
        filename = os.path.dirname(__file__) + '/chromedriver'
        driver = webdriver.Chrome(filename, chrome_options=options)
        driver.get(url)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    except Exception as e:
        raise CrawlingError()
    finally:
        driver.close()


def _get_title(soup):
    try:
        title = soup.find('meta', property='og:title')['content']
    except:
        title = None

    if title == None:
        try:
            title = soup.find('title').text
        except:
            title = None

    if title == None:
        try:
            title = soup.find('h1').text
        except:
            title = None

    if title == None:
        return ''
    else:
        title = title.replace('[', '\[')
        title = title.replace(']', '\]')
        return title


def find_title(url):
    soup = __load_page(url)
    title = _get_title(soup)
    _print_result(title=title, url=url)


def _print_result(title, url):
    print("[%s](%s){:target=\"_blank\"}" % (title, url))



if __name__ == '__main__':
    url = 'https://doitddo.tistory.com/84?category=855312'
    find_title(url)

