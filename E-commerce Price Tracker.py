import requests
from bs4 import BeautifulSoup
import pandas as pd

class E_Price_Tracker:

    # Extract html data from website 
    def extract_data(self, path):
        url = "https://www.mobgiz.com/mobile-phones-list"
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # save the html file 
        with open(path, 'w',  encoding='utf-8') as file:
            file.write(response.text)
    
    def clean_organized(self):
        data = []

        # open the html file for parsing 
        with open('mobgiz.html', 'r') as file:
            result = file.read()

            soup = BeautifulSoup(result, 'html.parser')
            mobile = soup.find_all('div', class_='product-info text-left')

            for mob in mobile:
                try:
                    specs_divs = mob.find_all("div", class_="col-sm-6")
                    specs = {}

                    for div in specs_divs:
                        label = div.find("span")
                        if not label:
                            continue
                        key = label.text.strip().replace(":", "")
                        value = div.text.replace(label.text, "").replace(":", "").strip()
                        specs[key] = value

                    # append all the data into data list 
                    data.append({
                    "Title" : mob.find('h3', class_="name").text,
                    "Price"  : mob.find('div', class_="product-price").text,
                     **specs
                    })
                except Exception as e:
                    continue
        
        # convert the list (data) into pandas dataframe
        df = pd.DataFrame(data)
        # save the dataframe as csv file
        df.to_csv('mobile.csv')

if __name__=="__main__":
    run = E_Price_Tracker()
    run.extract_data('mobgiz.html')
    run.clean_organized()


