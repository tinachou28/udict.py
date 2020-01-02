import requests
import errors
import objects
from bs4 import BeautifulSoup

def get_page(query):
    query2 = query.replace(" ", "%20")
    url = f"https://www.urbandictionary.com/define.php?term={query2}"
    page = requests.get(url)
    if page.status_code not in [200, 202]:
        raise errors.PageStatusError(page.status_code)
    soup = BeautifulSoup(page.content, "lxml")
    return objects.Page(soup)
        
        
        
    
    
