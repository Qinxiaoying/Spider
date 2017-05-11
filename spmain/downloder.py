#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2


class Html_Downloader(object):
    def download(self, url):
        if url is None:
            return None

        req = urllib2.urlopen(url)

        if req.getcode() != 200:
            return None
        return req.read()
