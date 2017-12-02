# -*- coding: utf-8
# !/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup
from lxml import etree

def start():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"}
    request = urllib2.Request("http://tieba.baidu.com/p/2166231880", headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    list_of_image = get_list_of_image(html)

    image_name = 1
    print "开始下载"
    for image_url in list_of_image:
        download_image(image_url, image_name)
        print "下载完成"+str(image_name)+'.jpg'
        image_name += 1;
    print "完成"


def get_list_of_image(html):
    """
    :param html: 从url得到的html文本内容
    :return:
    """
    # rule_str = r'src="(.+?\.jpg)"'
    # pattern = re.compile(rule_str)
    # list_of_image_url = pattern.findall(html)
    # for image_url in list_of_image_url:
    #     print image_url
    selector = etree.HTML(html)
    links = selector.xpath('//img[@class="BDE_Image"]/@src')
    return links


def download_image(image_url, image_name):
    pic = urllib2.urlopen(image_url).read()
    with open(str(image_name)+".jpg", 'w') as image_file:
        image_file.write(pic)
        image_file.close()

if __name__ == '__main__':
    start()