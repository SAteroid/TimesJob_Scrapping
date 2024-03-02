from bs4 import BeautifulSoup
import requests
import time


print('skills that are not familiar ')
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    # print(html_text)
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    # print(jobs)
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as x:
                    x.write(f'Company name: {company.strip()}\n')
                    x.write(f'Skills required: {skills.strip()}\n')
                    x.write(f'More Info:{more_info}\n')
                print(f'file saved:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60)