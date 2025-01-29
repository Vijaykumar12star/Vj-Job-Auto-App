import requests
from bs4 import BeautifulSoup
import json

def scrape_jobs(keywords, location):
    url = f"https://www.indeed.com/jobs?q={keywords}&l={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    for job in soup.find_all('div', class_='job_seen_beacon'):
        title = job.find('h2').text.strip()
        company = job.find('span', class_='companyName').text.strip()
        description = job.find('div', class_='job-snippet').text.strip()
        
        jobs.append({
            'title': title,
            'company': company,
            'description': description
        })
    
    return json.dumps(jobs[:5])  # Return first 5 results for demo
