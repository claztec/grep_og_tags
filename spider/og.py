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
        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
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
            title = soup.find('h1').text
        except:
            title = None

    if title == None:
        return ''
    else:
        title = title.replace('[', '\[')
        title = title.replace(']', '\]')
        return title


def get_meta(url):
    soup = __load_page(url)
    title = _get_title(soup)
    return (url, title)


def _print_result(result):
    print("[%s](%s){:target=\"_blank\"}" % (result[1], result[0]))



if __name__ == '__main__':
    # url = sys.argv[0]
    url = 'https://cnpnote.tistory.com/entry/PYTHON-%EA%B0%80%EC%A0%B8-%EC%98%A4%EA%B8%B0-%EC%98%A4%EB%A5%98-No-module-named-does-exist'
    result = get_meta(url)
    _print_result(result)
