
from urllib2 import urlopen
from bs4 import BeautifulSoup

def fetch(link):

    content = urlopen(link)
    soup = BeautifulSoup(content.read(), 'html.parser')
    # now to fetch all the data that we need
    all_data = soup#.findAll("li", {"class": "list-group-item"})  # all the data we need
    print all_data


link="https://github.com/uzunali"
fetch(link)