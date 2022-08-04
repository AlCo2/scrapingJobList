import requests
from bs4 import BeautifulSoup
import time

def scrap():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        date_pub = job.find('span', class_ = "sim-posted").span.text
        if 'few' in date_pub:
            company_name = job.find('h3',class_ = "joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            link = job.header.h2.a['href']
            with open(f'scrapeSucced/{index}.txt', 'w') as f:
                f.write(f'company name:{company_name.strip()} \n')
                f.write(f"skills:{skills.strip()} \n")
                f.write(f"link:{link} \n")
            print(f'file saved:{index}')
if __name__ == '__main__':
    while True:
        scrap()
        print('wait....')
        time_wait = 10
        time.sleep(time_wait * 60)
