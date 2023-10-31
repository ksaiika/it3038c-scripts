import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.scrapethissite.com/pages/simple/")

soup = BeautifulSoup(response.content, "html.parser")

cdivs = soup.find_all("div", class_="col-md-4 country")

print("Here is a list of countries starting with K and some relevant data: ")

for cdiv in cdivs:
	h3 = cdiv.find("h3", class_="country-name")
	cap = cdiv.find("span", class_="country-capital")
	pop = cdiv.find("span", class_="country-population")

	if h3 and cap and pop:
		cname = h3.get_text(strip=True)
		capL = cap.get_text(strip=True)
		popN = pop.get_text(strip=True)

	if cname.startswith("K"):
		print(f"{cname}, the capital is {capL}, the population is {popN}.")

