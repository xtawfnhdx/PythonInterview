import os
import json
import random
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from bs4 import BeautifulSoup

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

FILE_LOCLA_PATH = "reptile_01"


def parse_url_model(url):
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


def crawling_data_by_tag(tagList, maxpage, is_basic_tag):
    """
    开始执行爬取数据入口
    :param tagList: 数据类型标签
    :param maxpage: 爬取最大页数
    :param is_basic_tag: 是否为基础标签
    :return:
    """
    for tag in tagList:
        bookInfoList = []
        for page in range(maxpage):
            print(f'"{tag}"标签的第{page + 1}页开始执行')
            bookListPageUrl = f"https://book.douban.com/tag/{quote(tag)}?start={page * 20}&type=S"
            bookInfoList.extend(get_book_list_info(bookListPageUrl))
        save_book_info(bookInfoList, tag)


def get_book_list_info(bookListUrlByTarget):
    """
    循环图书URL里面的书籍列表
    :param bookListUrlByTarget:图书列表信息
    :return:爬取到的图书列表数据
    """
    bookList = []
    bookListSend = parse_url_model(bookListUrlByTarget)
    booklistObj = bookListSend.find('ul', {'class': 'subject-list'})
    booklist = booklistObj.find_all('li', {'class': 'subject-item'})
    for book in booklist:
        bookDetailUrl = book.find('a', {'class': 'nbg'}).get('href')
        bookInfo = get_book_info(bookDetailUrl)
        # 无评论或者评论人数太少，不爬取数据
        if int(bookInfo['BookDetails']['ScoreCount']) > 0:
            bookInfo["BookComment"] = get_book_comment(bookDetailUrl + 'comments/')
        else:
            bookInfo["BookComment"] = {}
        bookList.append(bookInfo)
    return bookList


def get_book_info(bookInfoUrl):
    """
    获取图书详情
    :param bookInfoUrl:图书详情地址
    :return:
    """
    bookInfoDic = {}
    try:
        bookInfoSoup = parse_url_model(bookInfoUrl)
        bookDetailStr = bookInfoSoup.find('div', {'id': 'info'}).text
        inf = re.sub(' +', '', re.sub('\n +', ' ', bookDetailStr))
        bookDetailDic = analysis_book_detail(inf)

        bookTitle = bookInfoSoup.find('span', {'property': 'v:itemreviewed'}).text
        print(f'《{bookTitle}》开始执行')

        bookInfoDic['BookTitle'] = bookTitle
        bookInfoDic['BookUrl'] = bookInfoUrl
        bookDetailDic['BookImage'] = [
            bookInfoSoup.find('div', {'id': 'mainpic'}).find('a').get('href'),
            bookInfoSoup.find('div', {'id': 'mainpic'}).find('img').get('src')
        ]
        bookScoreMoel = bookInfoSoup.find('div', {'id': 'interest_sectl'})
        if '无人评价' in bookScoreMoel.text or '人数不足' in bookScoreMoel.text:
            bookDetailDic['Score'] = 0
            bookDetailDic['ScoreCount'] = 0
        else:
            bookDetailDic['Score'] = bookScoreMoel.find('strong', {'class': 'll rating_num'}).text
            bookDetailDic['ScoreCount'] = bookScoreMoel.find('span', {'property': 'v:votes'}).text
        bookInfoDic['BookDetails'] = bookDetailDic
        return bookInfoDic
    except Exception as e:
        print(e)


def get_book_comment(bookCommentUrl):
    """
    获取图书评论
    :param bookCommentUrl:
    :return:
    """
    try:
        bookCommentListDic = []
        bookCommentSoup = parse_url_model(bookCommentUrl)
        bookCommentListObj = bookCommentSoup.find('div', {'class': 'comment-list new_score'}).find_all('li')
        for commentObj in bookCommentListObj:
            if len(bookCommentListDic) > 10:
                break;
            bookComment = {}
            commentUserObj = commentObj.find('span', {'class': 'comment-info'})
            bookComment['UserName'] = commentUserObj.find('a').text
            bookComment['UserCommentData'] = commentUserObj.find('span', {'class': 'comment-time'}).text
            bookComment['UserComment'] = commentObj.find('span', {'class': 'short'}).text
            bookCommentListDic.append(bookComment)
        return bookCommentListDic
    except Exception as e:
        print(e)


def analysis_book_detail(bookInfoStr):
    """
    分析图书详情文本信息
    :param bookInfoStr:包含图书信息的文本字符串
    :return: 图书信息字典
    """
    bookDetailsDic = {}
    infoList = bookInfoStr.split('\n')
    for info in infoList:
        if '作者' in info:
            bookDetailsDic["authorInfo"] = info.split(':')[1]
        if '出版社' in info:
            bookDetailsDic["press"] = info.split(':')[1]
        if '出版年' in info:
            bookDetailsDic["year"] = info.split(':')[1]
        if '页数' in info:
            bookDetailsDic["pages"] = info.split(':')[1]
        if '定价' in info:
            bookDetailsDic["price"] = info.split(':')[1]
        if 'ISBN' in info:
            bookDetailsDic["ISBN"] = info.split(':')[1]
    return bookDetailsDic


def save_book_info(bookInfoList, target):
    print('开始写入文件')
    fileFullName = os.path.join(FILE_LOCLA_PATH, target) + '.json'
    if os.path.exists(fileFullName):
        os.remove(fileFullName)
    with open(fileFullName, 'w', encoding='utf-8') as f:
        f.write(json.dumps(bookInfoList, ensure_ascii=False))
    print('写入文件完成')


if __name__ == "__main__":
    if not os.path.exists(FILE_LOCLA_PATH):
        os.makedirs(FILE_LOCLA_PATH)
    # tag = ['小说','历史','科普']
    tag = ['创新', '奇怪']
    crawling_data_by_tag(tag, 2, True)
