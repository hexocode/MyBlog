# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests,sys
import datetime

if __name__=='__main__':
	reurl = input("http://mp.weixin.qq.com/s?__biz=MzI1OTc5NTA2OA==&mid=100000129&idx=1&sn=7d4a0b20571164ee4f9dfb1a1da99d57&chksm=6a7230925d05b984bfa4948db48475b5566dc725cd2b9bf5d5252484692ad323da716348af77")
	req=requests.get(url=reurl)
	bf=BeautifulSoup(req.text,"html.parser")
	texts=bf.find_all('div',class_='rich_media_content')
	title=bf.find_all('h2',class_='rich_media_title')
	title=str(title[0].text)
	title=title[63:-82]
	title.replace('\n','')

	path=title+'.md'
	print(path)
	texts=(str(texts[0]).replace('data-src','src'))
	texts.replace('data-copyright="0"','')
	texts.replace('data-w','test1')
	write_flag=True
	with open(path,'a',encoding='utf-8') as f:
		f.write('---\ntitle: '+title+'\n')
		f.write('copyright: '+'true'+'\n')
		f.write('permalink: '+'1'+'\n')
		f.write('date: '+str(datetime.date.today())+'\n')
		f.write('updated: '+str(datetime.date.today())+'\n')
		f.write('tags: '+'tag'+'\n')
		f.write('categories: '+'tag'+'\n---\n\n')
		f.writelines(str(texts))