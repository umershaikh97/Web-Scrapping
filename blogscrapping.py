# Get github username and put it in .csv

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://github.com/umershaikh97?tab=repositories')

soup = BeautifulSoup(response.text,'html.parser')


with open('example.csv','w') as csv_file :
    csv_writer = writer(csv_file)
    headers=['username','description']
    csv_writer.writerow(headers)

    githubUserName = soup.find(class_='p-name vcard-fullname d-block overflow-hidden').getText()
    print(githubUserName)
    githubUserDescription = soup.find(class_='p-note user-profile-bio js-user-profile-bio').getText()
    print(githubUserDescription)
    csv_writer.writerow([githubUserName,githubUserDescription])


