from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from bs4 import BeautifulSoup
import os
import random

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

book_info_list = {}
book_info_one = {}

FILE_LOCLA_PATH = "reptile_01"


def checkbookinfo():
    pass


def checkbookbyid():
    pass


def parse_book_info(url):
    """
    解析URL
    :param url:需要解析的url
    :return: 返回html页面code
    """
    try:
        req = Request(url, headers=random.choice(USER_AGENTS))
        source_code = urlopen(req).read()
        htmlcode = str(source_code, 'utf-8')
        soup = BeautifulSoup(htmlcode, "lxml")
        return soup
    except (HTTPError, URLError) as e:
        print(e)


def begin_book(booktag, maxpage, is_basic_tag):
    """
    开始执行爬取数据入口
    :param booktag: 数据类型标签
    :param maxpage: 爬取最大页数
    :param is_basic_tag: 是否为基础标签
    :return:
    """
    for tag in booktag:
        for page in range(maxpage):
            bookListPageUrl = f"https://book.douban.com/tag/{quote(tag)}?start={page * 20}&type=S"
            loop_book_url(bookListPageUrl)


def loop_book_url(bookListUrl):
    """
    循环图书URL里面的书籍列表
    :param bookListUrl:
    :param tag:
    :return:
    """
    bookListSend = parse_book_info(bookListUrl)
    booklistObj = bookListSend.find('ul', {'class': 'subject-list'})
    booklist = booklistObj.find_all('li', {'class': 'subject-item'})
    for book in booklist:
        bookhref = book.find('a', {'class': 'nbg'}).get('href')
        get_book_info(bookhref)


def get_book_info(bookInfoUrl):
    """
    获取图书详情
    :param bookInfoUrl:
    :return:
    """
    bookInfoSoup = parse_book_info(bookInfoUrl)
    bookTitle = bookInfoSoup.find('span', {'property': 'v:itemreviewed'}).text
    imageDiv = bookInfoSoup.find('div', {'id': 'mainpic'})
    bookImage = [
        imageDiv.find('a').get('href'),
        imageDiv.find('img').get('src')
    ]
    bookInfoDiv = bookInfoSoup.find('div', {'id': 'info'})
    authorInfo = ''
    pubInfo = '',


def get_book_comment(bookCommentUrl):
    """
    获取图书评论
    :param bookCommentUrl:
    :return:
    """
    pass


if __name__ == "__main__":
    if not os.path.exists(FILE_LOCLA_PATH):
        os.makedirs(FILE_LOCLA_PATH)
    tag = ['小说']
    begin_book(tag, 2, True)
