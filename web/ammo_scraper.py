import requests
import json

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config.model import Ammunition

# The default URL is ammobuy.com
# Currently only searches through the first page.


def scrape_ammunition_info(url):

    # Get Caliber from URL
    caliber = url.split("/ammo/")[-1]

    # Add url string to default to searching only free shipping
    url += "&ship=0"  # Append "&ship=0" to the URL

    # Get URL response
    response = requests.get(url)
    html_content = response.content

    # Parse using BS
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all HTML elements with the specified classes
    cpr_elements = soup.select("td.ammo-info.ammo-ppr.sort-selected")
    href_elements = soup.select("a[href^='/go/']")
    total_price_elements = soup.select("span[itemprop='price']")
    rounds_elements = soup.select("td.ammo-info.ammo-rounds")
    grains_elements = soup.select("td.ammo-info.ammo-grains")
    retailer_elements = soup.select("a[href^='/retailer/']")

    # Extract the text values and href attributes
    cpr = [element.get_text(strip=True) for element in cpr_elements]
    href = [urljoin(url, element['href']) for element in href_elements]
    total_price = ["$" + element.get_text(strip=True) for element in total_price_elements]
    rounds = [element.get_text(strip=True) for element in rounds_elements]
    grain = [element.get_text(strip=True) for element in grains_elements]
    retailer = [element['href'].split("/retailer/")[-1] for element in retailer_elements]

    # Create Ammunition Obj
    result = zip(cpr, total_price, rounds, grain, retailer, href)

    # print(result)
    # Print the pairs with the caliber
    ammo_collection = []
    for cpr, total_price, rounds, grain, retailer, href in result:
        ammo_obj = Ammunition(caliber, cpr, total_price, rounds, grain, retailer, href)
        # print("--------------------")
        print(ammo_obj)
        ammo_collection.append(ammo_obj)
    # print(ammo_collection)
    

def read_urls_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['urls']


file_path = './config/urls.json'
urls = read_urls_from_json(file_path)

# Scrape each caliber specific webpage
for url in urls:
    scrape_ammunition_info(url)
