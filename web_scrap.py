###########################################################################################
#   Created by Jason Downing                                                              #
#   Some code originally found at this Stackoverflow Post:                                #
#   https://stackoverflow.com/questions/18966368/python-beautifulsoup-scrape-tables       #
#   Also this page as well:                                                               #
#   http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/  #
###########################################################################################

# To setup urllib2 / bs4 (BeautifulSoup)
# Follow this URL: http://linuxconfig.org/how-to-install-python3-beautiful-soup-environment-on-debian-linux
# and run this: pip install requests

import requests
from bs4 import BeautifulSoup

# Change to whatever your url is
url = "http://www.waterville.com/ski-ride/snow-report.html"

# Get the page, then grab just the text and use BeautifulSoup to work some magic on it.
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, "lxml")

# Now we've got just the HTML and can do some fun stuff with BeautifulSoup.
#print (soup)

# Let's try and get just the data for the ski conditions.

# THIS RETURNS EMPTY ARRAY ([])
#ski_data = soup.find_all("div", class_="tabset_content")

# THIS WORKS
ski_data = soup.findAll('div', {'class' : 'tabset_content'})

# Testing. This should be all the lift / trail data we need to parse.
#print (ski_data)

# Let's get all open trails.
#open_trails = soup.findAll('li', {'class' : 'open'})
#print (open_trails)

print ("*** Open lifts / trails: ***\n")

for each_div in soup.findAll('li', {'class' : 'open'}):
  print (each_div.text)

# Also all closed trails.
# closed_trails = soup.findAll('li', {'class' : 'closed'})
# print (closed_trails)

print ("\n\n*** Closed lifts / trails: ***\n")

for each_div in soup.findAll('li', {'class' : 'closed'}):
  print (each_div.text)
