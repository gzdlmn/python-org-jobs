import requests
from bs4 import BeautifulSoup

#IF YOU HAVE MANY PAGE

# ÖRNEK 3

url = "https://www.python.org/jobs"
r = requests.get(url)
print(r.status_code)
#200 oke
#print(r.content)
soup = BeautifulSoup(r.content, "lxml")
#print(soup)

pages = len(soup.find_all("ul", attrs={"class": "pagination"})[0].find_all("li"))-2
#print(pages)

total_jobs = 0

for page_number in range(1,pages+1):
    page_request_number = requests.get("https://www.python.org/jobs/?page=" + str(page_number))
    #print(page_request_number.url)
    page_soup = BeautifulSoup(page_request_number.content, "lxml")
    jobs = soup.find("div", attrs={"class": "row"}).ol.find_all("li")
    #print(jobs)
    for job in jobs:
        name = job.h2.find("a").text  
        #print(name)
        location = job.find("span", attrs={"class": "listing-location"}).text
        #print(location)
        company = job.find("span", attrs={"class": "listing-company-name"}).br.next.strip()
        #print(company)
        publish_time = job.find("time").text
        #print(publish_time)
        total_jobs += 1
        print(name, company, location, publish_time, sep="\n")
        print("-"*30)
print("Toplam {} adet iş bulundu.".format(total_jobs))