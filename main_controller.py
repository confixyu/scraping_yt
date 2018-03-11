import requests
from bs4 import BeautifulSoup
#import urllib2
import html5lib
import sys


titulo = "vacio"

class Main_controller():
	def soup(url):
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		return soup

	def title(soup):
		g_data_title = soup.find_all("span", {"class": "watch-title"})
		for item in g_data_title:
			titulo = item.text
		titulo = titulo.replace('\n', '')
		titulo = titulo.replace(' ', '')
		print(titulo)
		return titulo

	def channel(soup):
		g_data_channel = soup.find_all("div", {"class": "yt-user-info"})
		for item in g_data_channel:
			canal = item.text
		canal = canal.replace('\n', '')
		canal = canal.replace(' ', '')
		print(canal)
		return canal

	def like(soup):
		g_data_like = soup.find("button",attrs={"title": "I like this"}).get_text()
		like = str(g_data_like)
		print(like)
		return like

	def dislike(soup):
		g_data_dislike = soup.find("button",attrs={"title": "I dislike this"}).get_text()
		dislike = str(g_data_dislike)
		print(dislike)
		return dislike

	def view(soup):
		g_data_view = soup.find("span", {"class": "view-count"})
		view = str(g_data_view.text)
		view = view.replace('views', '')
		print(view)
		return view

	def date(soup):
		date_info = soup.find('strong', 'watch-time-text').get_text()
		publish_date = date_info.replace("Published on ", "")
		print(publish_date)
		return  publish_date


	"""def url():
		temp = 'temp.txt'
		file = open(temp,'r')
		url = file.readline()
		file.close()
		#print(url)
		return url"""


"""if __name__ == '__main__':
	url = "https://www.youtube.com/watch?v=w9YhKyQk-44"
	s = Main_controller.soup(url)
	Main_controller.title(s)"""