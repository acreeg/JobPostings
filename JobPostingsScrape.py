import requests
import datetime

now = datetime.datetime.now()
str_now = str(now)
html_now = ("<date>" + "DATE_TIME_STAMP: " + str_now + "</date>" + "\n")

jobPostings = {'StackOverflow' : 'http://stackoverflow.com/jobs?location=Nashville%2C+TN&range=50&distanceUnits=Miles', 
	'Emma' : 'http://careers.myemma.com/careers', 
	'DigitalReasoning' : 'http://www.digitalreasoning.com/job-search', 
	'Eventbrite' : 'https://jobs.lever.co/eventbrite?by=location',
	'Stratasan' : 'http://stratasan.com/about/careers/',
	'ArborHealth' : 'http://www.arborhealth.com/careers.html',
	'Rustici' : 'http://rusticisoftware.com/work-here/open-positions/',
	'Acxiom' : 'https://acxiom.wd5.myworkdayjobs.com/AcxiomUSA/jobs',
	'Aspect' : 'https://careers-aspect.icims.com/jobs/search?ss=1&searchLocation=13563-13608-Brentwood',
	'Qualifacts' : 'http://www.qualifacts.com/careers/',
	'CentreSource' : 'https://centresource.com/about/',
	'HCA' : 'http://careersathca.com/careers/search.dot?jobClass=InformationTechnology&state=Tennessee&perPage=100',
	'UBS' : 'https://jobs.ubs.com/tgwebhost/searchresults.aspx?SID=^8mpaQjHOFno945snBWzuAQNc2SVgO_slp_rhc_vPaH_slp_rhc_rUzc38aRMyAt/VRIFmXNF3c_slp_rhc_ZXUCt',
	'Parallon' : 'https://hca.taleo.net/careersection/newparallonkeywordssvcscorp/jobsearch.ftl',
	'Healthways' : 'http://healthways.jobs/jobs/',
	'Bridgestone' : 'http://bridgestoneamericas.jobs/jobs/?location=Nashville%2C+TN&q=Technology#1',
	'Indeed' : 'http://www.indeed.com/jobs?as_and=&as_phr=&as_any=developer+or+software+or+analytics+-manager+-project+-director+-administrative+-administrator+-sales+-receptionist+-account+-accounts+-video+-customer+-office+-writer&as_not=&as_ttl=&as_cmp=&jt=all&st=&sr=directhire&salary=&radius=50&l=Nashville,+TN&fromage=any&limit=100&sort=&psf=advsrch',
	'Dice' : 'https://www.dice.com/jobs/advancedResult.html?for_one=Software+Web+Developer+Data+Analytics+Science+Scientist+App&for_all=&for_exact=&for_none=Manager+Sr.+Volt+Contract+Zycron+Thorndale+Cybercoders+Relocation+Onora+Half+Vaco+senior&for_jt=&for_com=&for_loc=37212&jtype=Full+Time+OR+Part+Time&sort=relevance&limit=100&radius=50&jtype=Full+Time+OR+Part+Time&searchid=7662320480676',
	'Metova' : 'https://metova.com/jobs/',
	'Aloompa' : 'http://aloompa.com/jobs',
	'Leankit' : 'http://leankit.com/blog/leankit-home/jobs/',
	'Atiba' : 'http://www.atiba.com/careers/',
	'ParamoreDigital' : 'http://paramoredigital.com/careers/'}
	
	# Problem with the Cigna scrape on previous run ... 5_28_16
	#'Cigna' : 'https://cigna.taleo.net/careersection/cg_external_us/jobsearch.ftl?lang=en&radiusType=K&location=100100663&searchExpanded=false&radius=1',
	
for name, link in jobPostings.items():
	response = requests.get(link)
	html = response.content

	fileName = name + '.html'
	outfile = open(fileName, "a")
	outfile.write(html_now)
	outfile.close()

	outfile = open(fileName, "ab")
	outfile.write(html)
	outfile.close()