# Function receives 2 string value and return float value
# Fx value1='btc' and value2='usd' function make request in google 1btc to usd, load this page and return float value from google page
# Program can receive different valutes fx value1='dkk' value2='eur' or another

# 
# libs
# 
import requests, bs4

# 
# functions
# 

# parser
def parseData(valute1: str, valute2: str) -> float:
    # link to request
    url = "https://www.google.com/search?q=1%s+to+%s" % (valute1, valute2)
    
    # get page
    data = requests.request("GET",url)
    
    # converting to bs format
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    
    # searching items by html class
    this_data = soup.select(".iBp4i")
    
    # get second item and delete spaces
    arr = this_data[1].get_text().split(" ")

    # converting from str to float and return
    return float(arr[0].replace(".","").replace(",","."))
