import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime


'''This is the simple news fatching code, from more than 1 website and show the appropriate news with current date_time'''
# website are (bbc news and theguardian) for news fatching 

class live_news:
    def d_live_news(self):
        url = 'https://www.theguardian.com/us-news/us-politics'
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        find = soup.find_all('span', class_='show-underline dcr-uyefka')
        print("-----------------------US POLITICS/ theguardian / bbc-----------------------")
        print(f"\n📅 Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for con in find:
            print(f"=>  {con.text}")

    def bbc_livenews(self):
        url = 'https://www.bbc.com/news/us-canada'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        find = soup.find_all('div', class_='sc-9d830f2a-0 eKWlJZ')
        print('----------------------------bbc---------------------------')
        print(f"\n📅 Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for con in find:
            print(f"=>  {con.text}")

class sports:
    def d_sports(self):
        url = 'https://www.theguardian.com/uk/sport'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        find = soup.find_all('span', class_='show-underline dcr-uyefka')
        print("-----------------------SPORTS theguardian / bbc-----------------------")
        print(f"\n📅 Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for con in find:
            print(f"=>  {con.text}")
        
    def bbc_sports(self):
        url = 'https://www.bbc.com/sport'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        find = soup.find_all('p', class_='ssrcss-1b1mki6-PromoHeadline exn3ah910')
        print('----------------------------bbc---------------------------')
        print(f"\n📅 Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for con in find:
            print(f"=>  {con.text}")

class culture:
    def d_culture(self):
        url = 'https://www.theguardian.com/uk/culture'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        find = soup.find_all('span', class_='show-underline dcr-uyefka')
        print("-----------------------CULTURE  theguardian / bbc-----------------------")
        print(f"\n📅 Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for con in find:
            print(f"=>  {con.text}")

    def bbc_culture(self):
        url = 'https://www.bbc.com/culture'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        find = soup.find_all('h2', class_='sc-9d830f2a-3 fWzToZ')
        print('----------------------------bbc---------------------------')
        print(f"\n📅 Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for con in find:
            print(f"=>  {con.text}")


# here the news are automatically updated in every few sec to avoid delay 

if __name__=='__main__':
    while True:
        try:
        
            d_live = live_news()
            d_live.d_live_news()
            time.sleep(4)
            d_live.bbc_livenews()

            s_live = sports()
            time.sleep(4)
            s_live.d_sports()
            time.sleep(4)
            s_live.bbc_sports()
            
            c_live = culture()
            time.sleep(4)
            c_live.d_culture()
            time.sleep(4)
            c_live.bbc_culture()
            time.sleep(4)
        
        except requests.RequestException as e:
            print(f"Error {e}")