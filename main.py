import requests
from bs4 import BeautifulSoup
import hashlib

url = "https://www.d20pfsrd.com/bestiary/monster-listings/fey/vilderavn/"
username = "Testbug Jones"
password = "TeStBuG"

s = requests
r = s.get(url)
r = BeautifulSoup(r.text, "html.parser")

#class="section15"


r = BeautifulSoup(r.text, "html.parser")
form = soup.find("form",{"id":"login_form"})

######
payload = dict([(t.get("name"),t.get("value","")) 
	for t in form.findAll("input")
	if t.get("name")
])


md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
payload["vb_login_username"] = username
payload["vb_login_password"] = password
payload["vb_login_md5password"] = md5
payload["vb_login_md5password_utf"] = md5

r = s.post(f"{url}/login.php", 
	params= {"do": "login"},
	data = payload
)

r = s.get(f"{url}/sheets")
soup = BeautifulSoup(r.text, "html.parser")
rows = soup.find("table").find_all("tr")[1:]
sheet_data = []
for row in rows:
	tds = row.find_all("td")
	download_link = f'{url}{tds[5].find("a")["href"]}'
	json = s.get(download_link)
	_.isEmpty({json})
	sheet_data.append({
		"name": tds[1].text.strip(),
		"template": tds[2].text.strip(),
		"game": tds[3].text.strip(),
		"download_link": download_link,
		
      #"json": json.json()
	})

#["statblock,description,title,skills"]

'''pull in each of the monster stats and display easier. parse incoming text for stats. will need to remove hyperlinks or organize them together for quick reference.'''
