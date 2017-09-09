class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output_html', 'w')
        font.write('<html><meta charset="utf-8">')
        fout.write('<body>')
        fout.write('<table>')

        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title']).encode('utf-8')
            fout.write("<td>%s</td>" % data['summary']).encode('utf-8')
            fout.write("</tr>")


        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        font2 = open('output2.md', 'w')
        font2.write('# 100 pices of Baidu Baike\n')

        # ASCII
        for data in self.data:
            font2.write("# %s\n" % data['title'].encode('utf-8'))
            font2.write("**[%s](%s)**\n" % (data['url'],data['url']))
            font2.write(">%s\n" % data['summary'].encode('utf-8'))
            font2.write("* * *\n")
