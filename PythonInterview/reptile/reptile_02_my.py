import os
import json
import random
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote

FILE_LOCLA_PATH = "reptile_02"

USER_AGENTS = [
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0'},
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'},
    {'User-Agent': 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)'},
    {
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'},
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'},
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}]


def download_page_by_tag(tag):
    """
    根据标签下载当前页面所有图片
    :param tag:标签
    :return:
    """
    # 验证发现站酷的登录界面，只是一个iframe弹层，可以忽略弹层
    page = 1
    tarMsg = quote(tag)
    zcoolUrl = f'https://www.zcool.com.cn/search/content.json?word={tarMsg}&cate=0&type=0&recommendLevel=0&time=0&hasVideo=0&city=0&college=0&sort=5&limit=20&column=4&page={page}'
    request = Request(zcoolUrl, headers=random.choice(USER_AGENTS))
    ss = str(urlopen(request).read(), 'utf-8')
    pageMsglist = json.loads(ss)
    for pageMsg in pageMsglist['data']['data']:
        pageMsgSub = get_url_model(pageMsg['object']['pageUrl'])
        aaaa=pageMsgSub.find('div',{'class':'work-show-box mt-40 js-work-content'}).find_all('div',{'class':'reveal-work-wrap js-sdata-box text-center'})
        for aa in aaaa:
            print(aa.find('img').get('src'))

    #
    # soupSearchPageList = get_url_model(zcoolUrl)
    # userPageList = soupSearchPageList.find('div', {'id': 'search-card-list'}). \
    #     find_all('div', {'class': 'card-box new-card-box'})
    # for soup in userPageList:
    #     userPageUrl = soup.find('a').get('href')
    #     down_page_by_pageurl(userPageUrl)
    #


def down_page_by_pageurl(pageUrl):
    pagesoup = get_url_model(pageUrl)
    userName = pagesoup.find('p', {'class': 'author-info-title'}).find('a')[0].text
    pageName = pagesoup.find('div', {'class': 'details-contitle-box'}).find('h2').text.split(' ')[0]
    pageListSoup = pagesoup.find_all('div', {'class': 'reveal-work-wrap js-sdata-box text-center'})
    for page in pageListSoup:
        page.find('img').get('src')


def save_page_by_url(file, url):
    data = urlopen(url).read()
    with file('./' + file + '/abc.jpg', 'wb') as f:
        f.write(data)
        f.close


def get_url_model(url):
    try:
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get(url)
        # htmlStr = driver.page_source

        req = Request(url, headers=random.choice(USER_AGENTS))
        htmlFlow = urlopen(req).read()
        htmlStr = str(htmlFlow, 'utf-8')
        soup = BeautifulSoup(htmlStr, 'lxml')
        return soup
    except (HTTPError, URLError) as e:
        print(e)
    except Exception as e:
        print('未知错误：', e)


if __name__ == '__main__':
    if not os.path.exists(FILE_LOCLA_PATH):
        os.makedirs(FILE_LOCLA_PATH)
    # tag = input('请输入要下载的图片标签内容')
    download_page_by_tag('世界')
