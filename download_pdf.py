import requests
from Web_Scrape_Tool.web_scrape_tool import get_soup_adv
from bs4 import BeautifulSoup
import re
import os

import warnings
warnings.filterwarnings("ignore")
    
def download_pdf(pdf_link, title):
    # Download the PDF content
    response = requests.get(pdf_link, verify=False)
    
    if not os.path.exists("./PDFs"):
        os.makedirs("./PDFs")
        
    file_name = f"./PDFs/{title}"
    os.system(f"touch ./PDFs/{title}")
    with open(file_name, "wb") as f:
        f.write(response.content)
        print(f"Saved {title}.")
        
    return

def extract_pdf_link(pdf_string: str):
    # Filter out non-PDFs
    if ('.pdf' not in pdf_string):
        return False
    
    if ('//www.pdf' in pdf_string):
        return False

    res = None
    if "/url" in pdf_string:
        start_index = pdf_string.find("http")
        end_index = pdf_string.find(".pdf")
        res = pdf_string[start_index:end_index+4]
        # print(res)
        return res
    else:
        res = re.match(r"(http).*(\.pdf)", pdf_string)

    if not res:
        print("Bad String")
        return False
    
    res = res.group(0)
    return res

def extract_pdf_title(link):
    return link.text

def get_all_pdf_links(url: str):
    links = []
    titles = []
    
    pdf_soup = get_soup_adv(url)
  
    for link in pdf_soup.find_all('a'):
        
        link_href = link.get('href', [])
        res = extract_pdf_link(link_href)
        title = extract_pdf_title(link)
        if not (res): continue
        links.append(res)
        titles.append(title)
    
    return links, titles

# Scrapes and downloads all pdfs on a webpage
# Returns the number of pdfs
def download_pdfs(url: str):
    num_pdfs = 0
    
    # Get a hrefs links for PDFs
    hrefs, titles = get_all_pdf_links(url)
    for link, title in zip(hrefs, titles):
        download_pdf(link, title)
    
    return num_pdfs

def main():
    # url = input("Enter a url to scrape PDFs from: ")
    url = "https://www.google.com/search?q=electronics+pdf&rlz=1C1GCEU_enUS996US996&oq=electronics+pdf&aqs=chrome..69i57j0i131i433i457i512j0i402j0i433i512j0i131i433i512j69i65l3.6428j0j7&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIQCAEQABiDARixAxjJAxiABDIHCAIQABiSAzIKCAMQABixAxiABDINCAQQABiDARixAxiABDIGCAUQRRhBMgYIBhBFGEEyBggHEEUYQdIBCDY0MjhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
    num_pdfs = download_pdfs(url)
    
    
    
if __name__ == "__main__":
    main()