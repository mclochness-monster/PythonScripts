#scrapes stock price from yahoo

import urllib
import re
import sqlite3

conn = sqlite3.connect('test1.db')
print "Opened database successfully";

conn.execute("DROP TABLE IF EXISTS STOCKS")

conn.execute('''CREATE TABLE STOCKS
	(NAME TEXT PRIMARY KEY	NOT NULL,
	PRICE TEXT	NOT NULL);''')
print "Table created successfully";


#symbolName = ["aapl","goog","fb","nflx"]

tickerFile = open("tickers.txt")

tickerName = tickerFile.read()

newTickerName = tickerName.split("\n")

i=0
while i<len(newTickerName) :
	url = "http://finance.yahoo.com/q?s=" +newTickerName[i] +"&ql=1"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_'+newTickerName[i] +'">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	conn.execute("INSERT INTO STOCKS VALUES (?,?)", (newTickerName[i], price[0]));
	conn.commit()

	i+=1
