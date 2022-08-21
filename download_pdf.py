import requests
from Web_Scrape_Tool.web_scrape_tool import get_soup_adv
from bs4 import BeautifulSoup
import re
import json

import warnings
warnings.filterwarnings("ignore")
    
def download_pdf(pdf_link):
    # Download the PDF content
    response = requests.get(pdf_link)
    with open("PDFs", "wb") as f:
        f.write(response.content)
        print("Saved a PDF.")
    return

def extract_pdf_link(pdf_string: str):
    # Filter out non-PDFs
    if ('.pdf' not in pdf_string):
        return False
    
    if ('//www.pdf' in pdf_string):
        return False
    
    print(pdf_string)
    print()
    res = None
    if "/url" in pdf_string:
        # TODO: Need to implement when prefix is '/url'
        res = re.match(r", pdf_string")
    else:
        res = re.match(r"(http).*(\.pdf)", pdf_string)
        
    if not res:
        print("not")
        return False
    
    res = res.group(0)
    print(f"res: {res}\n")
    return True

def get_all_pdf_links(url: str):
    links = []
    
    pdf_soup = get_soup_adv(url)
    
    """
    REGEX: 
    
    ^wp.*php$
    
    start with wp and ends with php
    
    my example:
    
    (https).*.pdf
    
    """
    for link in pdf_soup.find_all('a'):
        
        link_href = link.get('href', [])
        res = extract_pdf_link(link_href)
        if not (res): continue
        links.append(res)
    
    return links

# Scrapes and downloads all pdfs on a webpage
# Returns the number of pdfs
def download_pdfs(url: str):
    num_pdfs = 0
    
    # Get a hrefs links for PDFs
    hrefs = get_all_pdf_links(url)
    # for link in hrefs:
    #     download_pdf(link)
    
    return num_pdfs

def main():
    # url = input("Enter a url to scrape PDFs from: ")
    url = "https://www.google.com/search?q=electronics+pdf&rlz=1C1GCEU_enUS996US996&oq=electronics+pdf&aqs=chrome..69i57j0i131i433i457i512j0i402j0i433i512j0i131i433i512j69i65l3.6428j0j7&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIQCAEQABiDARixAxjJAxiABDIHCAIQABiSAzIKCAMQABixAxiABDINCAQQABiDARixAxiABDIGCAUQRRhBMgYIBhBFGEEyBggHEEUYQdIBCDY0MjhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
    # num_pdfs = download_pdfs(url)
    extract_pdf_link("/url?esrc=s&q=&rct=j&sa=U&url=https://rnsinstituteoftechnology.org/wp-content/uploads/2020/04/principles-of-electronics-s-chand-v-k-mehta-rohit-mehta.pdf&ved=2ahUKEwj6nrKF39b5AhX-mmoFHeG4AWMQFnoECAIQAg&usg=AOvVaw1PyX1TcjZOD06_rwGj58Wy")
    
    
if __name__ == "__main__":
    main()