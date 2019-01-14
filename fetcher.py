from urllib2 import urlopen
from bs4 import BeautifulSoup

def fetch(link):

    content = urlopen(link)
    soup = BeautifulSoup(content.read(), 'html.parser')
    # now to fetch all the data that we need
    all_data = soup.find("div", {"id": "ember230"})  # all the data we need
    print all_data


link="https://itunes.apple.com/tr/app/t%C3%BCrk-hava-yollar%C4%B1-u%C3%A7ak-bileti/id1283414961?l=tr&mt=8"
fetch(link)