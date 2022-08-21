import requests
from Web_Scrape_Tool.web_scrape_tool import get_soup_adv
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")

def download_file(download_url):
    response = urllib3.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")
    
    
    
def download_pdf(pdf_link):
    # Download the PDF content
    response = requests.get(pdf_link)
    print(response.json())
    # with open() as f:
        
    return

def get_all_pdf_links(url: str):
    links = []
    
    pdf_soup = get_soup_adv(url)
    
    for link in pdf_soup.find_all('a'):
        # print(link)
        if ('.pdf' not in link.get('href', [])):
            continue
        
        links.append(link)
    
    return links

# Scrapes and downloads all pdfs on a webpage
# Returns the number of pdfs
def download_pdfs(url: str):
    num_pdfs = 0
    
    # Get a hrefs links for PDFs
    hrefs = get_all_pdf_links(url)
    for link in hrefs:
        download_pdf(link)
    
    return num_pdfs

def main():
    url = input("Enter a url to scrape PDFs from: ")
    num_pdfs = download_pdfs(url)
    
if __name__ == "__main__":
    main()