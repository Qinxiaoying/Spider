#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Html_Outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return None
        self.datas.append(data)

    def output_html(self):
        with open('./output/output.html', 'a+') as f:
            f.write('<html><head><meta charset="UTF-8"></head>')
            f.write("<body>")
            f.write("<table>")
            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>" % data['url'])
                f.write("<td>%s</td>" % data['title'].encode('utf-8'))
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")