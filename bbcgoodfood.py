from __future__ import print_function
from Adafruit_Thermal import *
from bs4 import BeautifulSoup
from thermal_addon import wrap_print as wp
import requests, sys

def fraction_checker(html_response):
	return

def main():
	printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
	response = requests.models.Response

	if len(sys.argv) > 1:
		try:
			# Need to mimic browser
			header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
			response = requests.get(sys.argv[1], headers=header)
		except:
			print("Are you sure you got the URL correct?")
	else:
		print("How can I do my job if I have no URL?")

	# Some dirty decoding
	dec_response = response.content.decode('utf-8')
	dec_response = dec_response.replace(u'\xbc', '1/4')
	dec_response = dec_response.replace(u'\xbd', '1/2')
	dec_response = dec_response.replace(u'\xbc', '3/4')
	dec_response = dec_response.replace(u'\u2013', '-')
	dec_response = dec_response.replace(u'\xa0', ' ')

	soup = BeautifulSoup(dec_response, 'html.parser')

	printer.boldOn()
	printer.setSize('M')
	title = soup.find("h1", attrs={"class": "recipe-header__title"}).text.strip()
	wp(title + "\n\n")
	
	printer.boldOff()
	printer.setSize('S')
	c_times_container = soup.find("div", attrs={"class": "recipe-details__text"})
	c_times = c_times_container.find_all("span")	
	wp("PREP: " + c_times[1].text + "\n")
	wp("COOK: " + c_times[3].text + "\n\n")

	printer.boldOn()
	printer.print("Ingredients:\n")
	printer.boldOff()

	ingredient_list = soup.find("ul", attrs={"class": "ingredients-list__group"})
	for ingredient in ingredient_list.contents:
		wp("- " + ingredient["content"].encode('ascii') + "\n")

	printer.boldOn()
	printer.print("\nMethod:\n")
	printer.boldOff()

	method_list = soup.find("ol", attrs={"class": "method__list"})
	counter = 1
	for instruction in method_list:
		wp(str(counter) + ". " + instruction.text.encode('ascii', 'replace') + "\n")
		counter += 1

	printer.feed(3)

if __name__ == '__main__':
    main()