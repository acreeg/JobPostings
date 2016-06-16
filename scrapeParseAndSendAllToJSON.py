import datetime
import requests
from bs4 import BeautifulSoup
import json


#Create dict for JSON Object
response = []

#Prepare for parsing Bridgestone with BeautifulSoup
urlBridgestone = 'http://bridgestoneamericas.jobs/jobs/?location=Nashville%2C+TN&q=Technology#1'
pageBridgestone = requests.get(urlBridgestone)
soupBridgestone = BeautifulSoup(pageBridgestone.content, 'lxml')

#Parse Bridgestone url
today = datetime.datetime.now().date()
for position in soupBridgestone.find_all('li', class_='direct_joblisting with_description'):

		
	if (position.h4 != None and position.h4.find('a') != None and position.h4.find('a').get('href') != None):
		jobid = position.h4.find('a').get('href').split('/')[3]
	else:
		jobid = 'None Given'
		
	if (position.h4 != None and position.h4.find('a') != None and position.h4.find('a').find('span', class_= 'resultHeader') != None and position.h4.find('a').find('span', class_= 'resultHeader').string != None):
		jobposition = position.h4.find('a').find('span', class_= 'resultHeader').string.strip()
	else:
		jobposition = 'None Given'
			
	if (position.h4 != None and position.h4.find('a') != None and position.h4.find('a').get('href') != None):
		jobdescription = 'http://bridgestoneamericas.jobs' + position.h4.find('a').get('href')
	else:
		jobdescription = 'None Given'
		
	if (position.find('div', class_= 'directseo_jobsnippet') != None and position.find('div', class_= 'directseo_jobsnippet').text != None):
		jobsummary = " ".join(position.find('div', class_= 'directseo_jobsnippet').text.split())
	else:
		jobsummary = 'None Given'
		
	jobsalary = 'None Given'
		
	jobemployer = 'Bridgestone Americas'
	
	joblocation = 'Nashville, TN'
	
	jobsource = 'Bridgestone Americas'
	
	jobdate = str(today)
	
	#Make changes to response for Bridgestone
	response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})

#Prepare for parsing Rustici with BeautifulSoup
urlRustici = 'http://rusticisoftware.com/work-here/open-positions/'
pageRustici = requests.get(urlRustici)
soupRustici = BeautifulSoup(pageRustici.content, 'lxml')

#Parse Rustici url
today = datetime.datetime.now().date()
for position in soupRustici.find_all('ul', class_='positions-list'):
	for position2 in position.find_all('li'):
		
		jobid = "None Given"
		
		if (position2.h4 != None and position2.h4.find('a') != None and position2.h4.find('a').string != None):
			jobposition = position2.h4.find('a').string.strip()
		else:
			jobposition = 'None Given'
			
		if (position2.h4 != None and position2.h4.find('a') != None):
			jobdescription = position2.h4.find('a').get('href')
		else:
			jobdescription = 'None Given'
		
		if (position2.find('p') != None and position2.find('p').string != None):
			jobsummary = position2.find('p').string.strip()
		else:
			jobsummary = 'None Given'
			
		if (position2.find('p') != None and position2.find('p').next_sibling != None and position2.find('p').next_sibling.string != None ):
			jobsummary = jobsummary + position2.find('p').next_sibling.string.strip()
		else:
			jobsummary = jobsummary
		
		jobsalary = 'None Given'
		
		jobemployer = 'Rustici'
	
		joblocation = 'Franklin, TN'
	
		jobsource = 'Rustici'
		jobdate = str(today)
	
		#Make changes to response for Rustici
	response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})

#Prepare for parsing HCA with BeautifulSoup
urlHCA = 'http://careersathca.com/careers/search.dot?jobClass=InformationTechnology&state=Tennessee&perPage=100'
pageHCA = requests.get(urlHCA)
soupHCA = BeautifulSoup(pageHCA.content, 'lxml')

#Parse HCA url
today = datetime.datetime.now().date()
for position in soupHCA.find_all('div', class_='row job-result'):
	
	if (position.find('div', class_='col-sm-12 col-sm-6') != None and position.find('div', class_='col-sm-12 col-sm-6').find('a') != None):
		Jobid = position.find('div', class_='col-sm-12 col-sm-6').find('a').get('href')
		jobid = Jobid.split('?jobId=')[1]
	else:
		jobid = 'None Given'
	
	if (position.find('div', class_='col-sm-12 col-sm-6') != None and position.find('div', class_='col-sm-12 col-sm-6').find('a') != None and position.find('div', class_='col-sm-12 col-sm-6').find('a').string != None):
		jobposition = position.find('div', class_='col-sm-12 col-sm-6').find('a').string.strip()
	else:
		jobposition = 'None Given'
	
	if (position.find('div', class_='col-sm-12 col-sm-6') != None and position.find('div', class_='col-sm-12 col-sm-6').find('a') != None):
		jobdescription = 'http://careersathca.com' + position.find('div', class_='col-sm-12 col-sm-6').find('a').get('href')
	else:
		jobdescription = 'None Given'
	
	if (position.find('div', class_='col-xs-3 col-sm-2') != None and position.find('div', class_='col-xs-3 col-sm-2').next_sibling != None and position.find('div', class_='col-xs-3 col-sm-2').next_sibling.next_sibling != None and position.find('div', class_='col-xs-3 col-sm-2').next_sibling.next_sibling.string != None):
		jobsummary = position.find('div', class_='col-xs-3 col-sm-2').next_sibling.next_sibling.string.strip()
	else:
		jobsummary = 'None Given'
		
	jobsalary = 'None Given'
	
	jobemployer = 'HCA'
	
	joblocation = position.find('div', class_='col-xs-3 col-sm-2').string.strip()
	
	jobsource = 'HCA'
	jobdate = str(today)
	
	#Make changes to response for HCA
	response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})

#Prepare for parsing Eventbrite with BeautifulSoup
urlEventbrite = 'https://jobs.lever.co/eventbrite?by=location'
pageEventbrite = requests.get(urlEventbrite)
soupEventbrite = BeautifulSoup(pageEventbrite.content, 'lxml')

#Parse Eventbrite url
today = datetime.datetime.now().date()
for position in soupEventbrite.find_all('div', class_='posting'):
	
	jobid = 'None'
	
	if (position.find('a', class_='posting-title') != None and position.find('a', class_='posting-title').h5 != None and position.find('a', class_='posting-title').h5.string != None):
		jobposition = position.find('a', class_='posting-title').h5.string.strip()
	else:
		jobposition = 'None Given'
		
	jobdescription = position.find('div', class_='posting-apply').a.get('href')
	
	if (position.find('a', class_='posting-title') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-commitment posting-category small-category-label') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-commitment posting-category small-category-label').string != None):
		jobsummary = position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-commitment posting-category small-category-label').string.strip()
	else:
		jobsummary = 'None Given'
		
	jobsalary = 'No Salary Listed'
	jobemployer = 'Eventbrite'
	
	if (position.a != None and position.find('a', class_='posting-title').find('div', class_='posting-categories') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-location posting-category small-category-label') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-location posting-category small-category-label').string != None):
		joblocation = position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-location posting-category small-category-label').string.strip()
	else: joblocation = 'None Given'
	
	if (position.a != None and position.find('a', class_='posting-title').find('div', class_='posting-categories') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-team posting-category small-category-label') != None and position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-team posting-category small-category-label').string != None):
		Jobteam = position.find('a', class_='posting-title').find('div', class_='posting-categories').find('span', class_='sort-by-team posting-category small-category-label').string.strip()
	else:
		Jobteam = 'None Given'
	
	jobsource = 'Eventbrite'
	jobdate = str(today)
	
	#Make changes to response for Eventbrite
	if (Jobteam == 'Engineering' and joblocation == 'Nashville, Tennessee'):
		response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})


#Prepare for parsing LeanKit with BeautifulSoup
urlLeanKit = 'http://leankit.com/blog/leankit-home/jobs/'
pageLeanKit = requests.get(urlLeanKit)
soupLeanKit = BeautifulSoup(pageLeanKit.content, 'lxml')

#Parse LeanKit url
today = datetime.datetime.now().date()
for position in soupLeanKit.find_all('div', class_='entry-content blog-post'):
	for position2 in position.ul.find_all('li'):
	
		jobid = 'None'
	
		if (position2 != None and position2.a != None):
			jobposition = position2.a.string.strip()

		jobdescription = position2.a.get('href')
		jobsummary = 'None'
		jobsalary = 'No Salary Listed'
		jobemployer = 'LeanKit'
		joblocation = 'Franklin, TN'
		jobsource = 'LeanKit'
		jobdate = str(today)
	
		#Make changes to response for LeanKit
		response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})


#Prepare for parsing StackOverflow with BeautifulSoup
urlStack = 'http://stackoverflow.com/jobs?location=Nashville%2C+TN&range=50&distanceUnits=Miles'
page = requests.get(urlStack)
soup = BeautifulSoup(page.content, 'lxml')

#Parse StackOverflow url
today = datetime.datetime.now().date()
for position in soup.find_all('div', class_='-item'):
	jobid = position.get('data-jobid')
	jobposition = position.a.string.strip()
	jobdescription = 'http://stackoverflow.com' + position.find('a')['href']
	jobsummary = 'No Summary Included'
	
	Salary = position.find('span', class_='salary')
	if Salary != None:
		jobsalary = " ".join(Salary.string.strip().split())
	else:
		jobsalary = 'No Salary Listed'
	
	jobemployer = position.find('li', class_='employer').string.strip()
	joblocation = position.find('li', class_='location').string.strip()
	jobsource = 'StackOverflow'
	jobdate = str(today)
	
	#Make changes to response for StackOverflow
	response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})
	

#Prepare for parsing Dice with BeautifulSoup
urlDice = 'https://www.dice.com/jobs/advancedResult.html?for_one=Software+Web+Developer+Data+Analytics+Science+Scientist+App&for_all=&for_exact=&for_none=Manager+Sr.+Volt+Contract+Zycron+Thorndale+Cybercoders+Relocation+Onora+Half+Vaco+senior&for_jt=&for_com=&for_loc=37212&jtype=Full+Time+OR+Part+Time&sort=relevance&limit=100&radius=50&jtype=Full+Time+OR+Part+Time&searchid=7662320480676'
pageDice = requests.get(urlDice)
soupDice = BeautifulSoup(pageDice.content, 'lxml')

#Parse Dice url
today = datetime.datetime.now().date()
for position in soupDice.find_all('div', class_='serp-result-content'):
	JobId = position.h3.a.find('span', class_='job-status-indicator icon-star-1 saveaction')
	if JobId != None:
		jobid = position.h3.a.find('span', class_='job-status-indicator icon-star-1 saveaction')['id']
	else:
		jobid = None
	
	Jobposition = position.h3.find('a')
	if Jobposition != None:
		jobposition = position.h3.find('a').get('title')
	else:
		jobposition = 'Still working on it'
	
	Jobdescription = position.h3.find('a')
	if Jobdescription != None:
		jobdescription = position.h3.find('a')['href']
	else:
		jobdescription = 'Still working on it'
		
	Jobsummary = position.find('div', class_='shortdesc')
	if (Jobsummary != None and Jobsummary.string != None):
		jobsummary = position.find('div', class_='shortdesc').string.strip()
	else:
		jobsummary = 'Still working on it'
		
	jobsalary = 'No Salary Listed'
	
	Jobemployer = position.ul.find('li', class_='employer').find('span', class_='hidden-xs')
	if Jobemployer != None:
		jobemployer = position.ul.find('li', class_='employer').find('span', class_='hidden-xs').get('title')
	else:
		jobemployer = 'Still working on it'
		
	Joblocation = position.ul.find('li', class_='location').find('span', class_='icon-compass-3')
	if Joblocation != None:
		joblocation = Joblocation.next_element
	else:
		joblocation = 'Still working on it'
	
	jobsource = 'Dice'
	
	jobdate = str(today)
	
	#Make changes to response for Dice
	if jobid != None:
		response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})


#Prepare for parsing Indeed with BeautifulSoup
urlIndeed = 'http://www.indeed.com/jobs?as_and=&as_phr=&as_any=developer+software+analytics&as_not=clients+manager+project+director+administrative+administrator+sales+receptionist+account+accounts+video+customer+office+writer&as_ttl=&as_cmp=&jt=all&st=&sr=directhire&salary=&radius=50&l=Nashville,+TN&fromage=any&limit=100&sort=&psf=advsrch'
pageIndeed = requests.get(urlIndeed)
soupIndeed = BeautifulSoup(pageIndeed.content, 'lxml')
	
#Parse Indeed url
today = datetime.datetime.now().date()
for position in soupIndeed.find_all('div', class_='  row  result'):
	jobid = position.get('data-jk')
	jobposition = position.a.get('title')
	jobdescription = 'http://indeed.com' + position.find('a')['href']
	
	Summary = position.table.tr.td.find('span', class_='summary')
	if (Summary != None and Summary.string != None):
		jobsummary = Summary.string.strip()
	else:
		jobsummary = 'No Summary Included'
		
	Salary = position.table.td.nobr
	if Salary != None:
		jobsalary = Salary.string.strip()
	else:
		jobsalary = 'No Salary Listed'
	
	Employer = position.find('span', class_='company')
	if (Employer != None and Employer.span != None and Employer.span.string != None):
		jobemployer = Employer.span.string.strip()
	elif (position.find('div', class_='sjcl') != None and position.find('div', class_='sjcl').span != None and position.find('div', class_='sjcl').span.string):
		jobemployer = position.find('div', class_='sjcl').span.string.strip()
	elif (Employer != None and Employer.span != None and Employer.span.a != None):
		jobemployer = Employer.span.a.string.strip()
	else:
		jobemployer = 'Employer is Unlisted'
		
	Location = position.find('span', class_='location')
	if Location.string != None:
		joblocation = Location.string.strip()
	elif (position.find('span', itemprop_="addressLocality") != None and position.find('span', itemprop_="addressLocality").string != None):
		joblocation = position.find('span', itemprop_="addressLocality").string.strip()
	else:
		joblocation = 'Unlisted'
		
	jobsource = 'Indeed'
	
	jobdate = str(today)
	
	#Make changes to response for Indeed
	response.append({'id' : jobid, 'position' : jobposition, 'description' : jobdescription,'summary' : jobsummary, 'employer' : jobemployer,'location' : joblocation,'salary' : jobsalary,'source' : jobsource,'active' : 1,'activated' : jobdate ,'closed' : 0,'revised' : 'N'})

#Write response to JSON file
postingsFile = '/Users/glennacree/Dropbox/DataScience/JobPostings/jobPostings.json'
with open(postingsFile,'a') as outfile:
 	json.dump(response, outfile, sort_keys=True)

outfile.close()
