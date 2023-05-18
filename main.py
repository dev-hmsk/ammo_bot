from web.ammo_scraper import scrape_ammo_info
from graphs.create_graph import cpr_graph
from jinja2 import Template
import json
import time 
import os

current_directory = os.getcwd()

START = True
def main():

    # Load urls from urls.json
    file_path = './config/urls.json'
    urls = read_urls_from_json(file_path)
    # Scrape each caliber specific webpage
    for url in urls:
        # Since each URL is defined by caliber each ammo_collection returned will be 
        # by default collected by shared caliber.
        current_date, caliber , ammo_collection = scrape_ammo_info(url)
        # Create Graph
        # Assigned as Bug #1
        # cpr_graph(ammo_collection, caliber, (f'{caliber} + {current_date}.png'))
        
        with open('template/ammunition_template.html') as file:
            template = Template(file.read())
            # Render the template with the ammunition data
            html_content = template.render(ammunition_list=ammo_collection, current_date=current_date)
        file_path=f'./emails/{caliber}_ammunition_email_{current_date}.html'
        with open(file_path, 'w') as file:
            file.write(html_content)
        
        print("Email HTML file created: ammunition_email.html")

# Print a message to confirm the file has been written

def read_urls_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['urls']

if __name__ == "__main__":
    while START == True:
        main()
        print('CANCEL HERE')
        time.sleep(10)
        
