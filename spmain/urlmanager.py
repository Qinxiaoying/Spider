#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Url_manager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, new_url):
        if new_url is None:
            return
        if new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)

    def add_new_urls(self, urls):
        if urls is None:
            return
        for url in urls:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_urls(self):
        return len(self.new_urls) != 0
