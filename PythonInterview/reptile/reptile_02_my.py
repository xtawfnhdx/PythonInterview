import os
import json
import random
import shutil
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
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


def download_page_by_tag(tag, page=1, totalcount=5):
    """
    ??????????????????????????????????????????
    :param tag: ??????
    :param page: ??????
    :param totalcount:??????????????????????????????
    :return:
    """
    nowNum = 1

    # ?????????????????????????????????json????????????????????????????????????????????????
    tarMsg = quote(tag)
    zcoolUrl = f'https://www.zcool.com.cn/search/content.json?word={tarMsg}&cate=0&type=0&recommendLevel=0&time=0&hasVideo=0&city=0&college=0&sort=5&limit=20&column=4&page={page}'
    request = Request(zcoolUrl, headers=random.choice(USER_AGENTS))
    responseDataStr = str(urlopen(request).read(), 'utf-8')
    responseDataList = json.loads(responseDataStr)

    for userPageUrlModel in responseDataList['data']['data']:
        if nowNum > totalcount:
            return
        if 'username' not in str(userPageUrlModel):
            continue

        userName = userPageUrlModel['object']['creatorObj']['username']
        userId = userPageUrlModel['object']['creatorObj']['id']
        pageName = re.sub('<[^<]+?>', '', userPageUrlModel['object']['title']).replace('\n', '').strip()

        print(f'????????????????????????{userName} ??? {pageName}')
        # ??????????????????????????????
        folderStr = f'./{FILE_LOCLA_PATH}/{userId}_{userName}_{pageName}'
        if os.path.exists(folderStr):
            shutil.rmtree(folderStr)
        os.makedirs(folderStr)

        userPageSoup = get_url_model(userPageUrlModel['object']['pageUrl'])
        imgModelList = userPageSoup.find('div', {'class': 'work-show-box mt-40 js-work-content'}).find_all('div', {
            'class': 'reveal-work-wrap js-sdata-box text-center'})

        for imgModel in imgModelList:
            save_img_by_url(imgModel.find('img').get('src'), folderStr)
        nowNum = nowNum + 1


def save_img_by_url(imgurl, folder):
    """
    ????????????
    :param imgurl:????????????
    :param folder: ???????????????
    :return:
    """
    imgName = imgurl.split('/')[-1].split('.')[0]
    urlretrieve(imgurl, f'{folder}/{imgName}.jpg')


def get_url_model(url):
    """
    ??????url?????????????????????
    :param url:
    :return:
    """
    try:
        req = Request(url, headers=random.choice(USER_AGENTS))
        htmlFlow = urlopen(req).read()
        htmlStr = str(htmlFlow, 'utf-8')
        soup = BeautifulSoup(htmlStr, 'lxml')
        return soup
    except (HTTPError, URLError) as e:
        print(e)
    except Exception as e:
        print('???????????????', e)


if __name__ == '__main__':
    if not os.path.exists(FILE_LOCLA_PATH):
        os.makedirs(FILE_LOCLA_PATH)
    tag = input('???????????????????????????????????????')
    download_page_by_tag(tag, 1, 10)
    # download_page_by_tag('??????', 1, 10)
