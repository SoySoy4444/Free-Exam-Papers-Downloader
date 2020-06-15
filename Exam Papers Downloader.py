#Created on June 12th, 2020
#Downloads papers from https://freeexampapers.com

import requests
from bs4 import BeautifulSoup
import os
import threading
import time

def download_paper(fileURL):
    url = baseURL + fileURL

    r = requests.get(url)

    print(os.path.join(folder_name, fileURL))

    with open(os.path.join(folder_name, fileURL), "wb") as f:
        f.write(r.content)

#given a list of all files 
def download():
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass 
    
    start = time.perf_counter()
    threads = []
    for fileURL in links[1:]:
        print(f"Downloading {fileURL}...")
        
        t = threading.Thread(target=download_paper, args=[fileURL,]) #start a new thread to download each paper
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")


while True:
    baseURL = input("Enter url of folder: ")

    sss = baseURL.split("/")
    print(sss)
    folder_name = " ".join(sss[4:])
    print(folder_name)


    html_content = requests.get(baseURL)
    soup = BeautifulSoup(html_content.content, "lxml")

    #If the <td> has <a>,  get the href.
    links = [td.find("a").get("href") for td in soup.findAll("td") if td.find("a") != None]

    threads = []

    download()
