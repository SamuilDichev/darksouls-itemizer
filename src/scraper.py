from typing import List

import requests
import csv
from bs4 import BeautifulSoup

from src.constants import TABLE_ROW_SELECTOR, HELMS_MAX_UPGRADE, CHEST_MAX_UPGRADE, \
	GLOVES_MAX_UPGRADE, PANTS_MAX_UPGRADE, BEAUTIFUL_SOUP_PARSER


class Scraper():
	def scrape_all_items(self):
		for url in (HELMS_MAX_UPGRADE, CHEST_MAX_UPGRADE, GLOVES_MAX_UPGRADE, PANTS_MAX_UPGRADE):
			output_file_name = url.split('/')[-1].replace('+', ' ')
			headers, items = self._scrape_item_table(url)

			with open('{}.csv'.format(output_file_name), 'w') as f:
				writer = csv.writer(f)
				writer.writerow(headers)
				for item in items:
					writer.writerow(item)

	def _scrape_item_table(self, url) -> (List, List):
		res = requests.get(url)
		soup = BeautifulSoup(res.content, BEAUTIFUL_SOUP_PARSER)
		rows = soup.select(TABLE_ROW_SELECTOR)

		headers_html = rows.pop(0)
		headers = ['Name']
		for header in headers_html.findAll('th'):
			img = header.find('img')
			if img:
				headers.append(img.get('alt').replace('-dark-souls', '').replace('-', ' ').capitalize())

		items = [[col.text for col in row.findAll('td')] for row in rows]
		return headers, items