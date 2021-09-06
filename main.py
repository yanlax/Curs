from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ad import Ui_Form
import sys
import requests 
from bs4 import BeautifulSoup
import time
ETHEREUM = 'https://www.google.com/search?q=ethereum+%D0%BA%D1%83%D1%80%D1%81&ei=SCXSYK-hCsSGrwTKwbPgBA&oq=ETHEREUM+&gs_lcp=Cgdnd3Mtd2l6EAEYATIHCAAQsQMQQzIFCAAQsQMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBQgAELEDMgoIABCxAxCDARBDMgIIADoHCAAQRxCwA1D0Alj0AmDXC2gAcAN4AIABhAGIAdUBkgEDMS4xmAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz'
BITCOIN = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+bitcoin&oq=%D0%BA%D1%83%D1%80%D1%81+Bi&aqs=chrome.1.69i57j0i433j0l8.17287j1j9&sourceid=chrome&ie=UTF-8'
EURO = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&ei=GyLSYO-hM6nnrgSCn6v4BQ&oq=%D0%BA%D1%83%D1%80%D1%81&gs_lcp=Cgdnd3Mtd2l6EAMYADIPCAAQsQMQgwEQQxBGEIICMgoIABCxAxCDARBDMgQIABBDMggIABCxAxCDATIECAAQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIHCAAQsQMQQzIHCAAQyQMQQzIECAAQQzoHCAAQRxCwAzoHCAAQsAMQQzoFCAAQsQM6AggAOgsILhCxAxDHARCjAlCyBliOHmDzJmgBcAJ4AIABf4gB_wSSAQMxLjWYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'
DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'	
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

app = QApplication(sys.argv)
Form =  QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


class Curs():

	def Dollar():
		full_page = requests.get(DOLLAR_RUB, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		ui.label_6.setText(str(convert) + ' Р')
	Dollar()

	def Euro():
		full_page = requests.get(EURO, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		ui.label_7.setText(str(convert) + ' Р')
	Euro()

	def Bitcoin():
		full_page = requests.get(BITCOIN, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		ui.label_8.setText(str(convert) + ' Р')
	Bitcoin()

	def Ethereum():
		full_page = requests.get(ETHEREUM, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		con = convert
		ui.label_9.setText(str(con) + ' Р')

	Ethereum()
		
curs = Curs()
sys.exit(app.exec_())
