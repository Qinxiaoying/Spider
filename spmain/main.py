#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlmanager
import urlparser
import downloder
import outputer


class Spider(object):
    def __init__(self):
        self.urls = urlmanager.Url_manager()
        self.downloader = downloder.Html_Downloader()
        self.parser = urlparser.Html_Parser()
        self.outputer = outputer.Html_Outputer()

    def craw(self, init_url):
        count = 1
        self.urls.add_new_url(init_url)
        while self.urls.has_new_urls:
            try:
                new_url = self.urls.get_new_url()
                html_content = self.downloader.download(new_url)
                #print html_content
                new_urls, new_data = self.parser.parser(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                print new_urls
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                print count
                count +=1
            except:
                print 'Failed'
        self.outputer.output_html()


if __name__ =='__main__':
    init_url = 'http://baike.baidu.com/item/Python'
    process = Spider()
    process.craw(init_url)
