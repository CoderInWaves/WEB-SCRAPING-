import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper_Analyzer:
    
    # Scrape data using url,and header
    def scraper(self, path):
        url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
        headers = {
            "User-Agent": "Mozilla/5.0",
        }

        response = requests.get(url, headers=headers)
        
        # Save the html data into a text file
        with open(path, "w", encoding="utf-8") as file:
            file.write(response.text)
            print("Data sucessfully written")
    
    # open and read that file you want to extract information 
    def clean_analyse(self):
        with open("Sequential Art.html", "r",encoding="utf-8") as f2:
            file = f2.read()
            
            # pass the hint according to html file 
            soup = BeautifulSoup(file, 'html.parser')          
            books = soup.find_all('article', class_='product_pod')
            
            # store all data that come from loop as a list 
            data = []
            
             # run a loop into the parse class and loop through all information on that class
            for book in books:
                
                # extract useful content using their specific tags
                title = book.h3.a['title']
                price = book.find('p', class_="price_color").text
                availbility = book.find('p', class_="instock availability").text.strip()
                
                # send all tage data into a list using a dict obj
                data.append({
                    'Title': title,
                    'Price': price,
                    'Availability': availbility
                })
            
            # convert the list into dataframe , pandas automatically filter and organized according to key as column 
            da = pd.DataFrame(data)
            print(da)                                 # print the dataframe


    
        
if __name__=="__main__":
    z = Scraper_Analyzer()
    # z.scraper(path="Sequential Art.html")
    z.clean_analyse()
  





