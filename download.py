from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import csv
import time
import re

def books(hundredLinkList):
  final_text = []
  for url in hundredLinkList:
    # ebookNum= url.split('/')[-1]
    link = url
    response = requests.get(url)
    page_content = BeautifulSoup(response.text, 'html.parser')

    text = page_content.find('a', class_= 'link')

    hrefs = text.get('href')
    final_text.append("https://www.gutenberg.org"+hrefs)
    
    
    print (final_text)
    return final_text


# need to clean up the code
if __name__ == '__main__':
    url = 'https://www.gutenberg.org/browse/scores/top'
    response = requests.get(url)
    page_content = BeautifulSoup(response.text, 'html.parser')

    href_tags = page_content.find_all(href=True)   
    hrefs = [tag.get('href') for tag in href_tags]

    needed_links = []
    for hreflink in hrefs:
        needed_links.append(hreflink)
        #print (hreflink)
    
    filtered_needed_links = filter(lambda k: 'ebooks' in k, needed_links)
    filtered_links_with_urls = []
    final_urls = []
    needed_url = 'https://www.gutenberg.org'
    # print(filtered_needed_links)

    count = 0
    for link in filtered_needed_links:
        if (count > 0 and count <= 1):
            final_url = needed_url + link
            final_urls.append(final_url)
        count = count + 1

    temp_final_links = []
    # print the final urls
    # print(final_urls)
    for final_url_link in final_urls:
        # print(final_url_link)

        temp_response = requests.get(final_url_link)
        temp_page_content = BeautifulSoup(response.text, 'html.parser')

        # print(temp_page_content)

        temp_href_tags = page_content.find_all(href=True)   
        temp_hrefs = [tag.get('href') for tag in href_tags]

        # print('temp href len')
        # print(len(temp_hrefs))

        for temp_href_link in temp_hrefs:
            temp_final_links.append(temp_href_link)
        
        temp_filtered_href_links = filter(lambda k: 'rtf' in k, temp_final_links)

        for link in temp_filtered_href_links:
            temp_final_url = needed_url + link
            # print(temp_final_url)
    # print(len(final_urls))

    books(final_urls)
