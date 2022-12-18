from urllib import request
import re
import time
import random
import psycopg
from hashlib import md5
from ua_info import ua_list
import sys

class MovieSkySpider:
    def __init__(self):
        self.url= 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.conn = psycopg.connect("host=localhost dbname=movieskydb user=postgres password=root")
        self.course = self.conn.cursor() 
    def get_html(self,url):
        headers={'User-Agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode('gb2312','ignore')
        return html
    def re_func(self,re_bds,html):
        pattern=re.compile(re_bds,re.S)
        r_list=pattern.findall(html)
        return r_list
    def parse_html(self,one_url):
        one_html=self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        link_list=self.re_func(re_bds,one_html)
        for link in link_list:
            two_url='https://www.dytt8.net' + link
            s=md5()
            s.update(two_url.encode())
            finger=s.hexdigest()
            if self.is_hold_on(finger):
                self.save_html(two_url)
                time.sleep(random.randint(1,2))
                ins='insert into request_finger values(%s)'
                self.course.execute(ins,[finger])
                self.conn.commit()
            else:
                sys.exit('更新完成')
    def is_hold_on(self,finger):
        sql='select finger from request_finger where finger=%s'
        r=self.course.execute(sql,[finger])
        if not r:
            return True
    def save_html(self,two_url):
        two_html=self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1> \
        </div>.*?<a.*?href="(.*?)".*?>.*?style="BACKGROUND-COLOR:.*?</a>'
        film_list=self.re_func(re_bds,two_html)
        print(film_list)
        sql = 'insert into movieinfo values(%s,%s)'
        self.course.executemany(sql,film_list)
        self.conn.commit()
    def run(self):
        for i in range(1,4):
            url=self.url.format(i)
            self.parse_html(url)
if __name__=='__main__':
    spider=MovieSkySpider()
    spider.run()