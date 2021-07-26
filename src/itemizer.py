import csv
import itertools
from typing import Dict


class Itemizer():
	def __init__(self, file_paths):
		self.items_by_type = self._load_items(file_paths)

	def _load_items(self, file_paths) -> Dict:
		items_by_type = {}
		for file_path in file_paths:
			with open(file_path, 'r') as f:
				reader = csv.DictReader(f)
				items = list(reader)
				# items.insert(0, self._create_empty_item_from_template_item(items[0]))
				items_by_type[file_path.split(' ')[0]] = items
		return items_by_type

	def _create_empty_item_from_template_item(self, template_item) -> Dict:
		empty_item = {}
		for k, v in template_item.items():
			if k == 'Name':
				empty_item[k] = 'Empty'
			elif isinstance(v, int) or isinstance(v, float):
				empty_item[k] = 0.0
		return empty_item

	def compute_and_save_all_possible_item_sets(self, output_file_name):
		items = list(self.items_by_type.values())
		cartesian_product = itertools.product(*items)

		with open(output_file_name, 'w') as f:
			writer = csv.DictWriter(f, items[0][0].keys())
			writer.writeheader()

			for item_combination in cartesian_product:
				item_set = {}
				for item in item_combination:
					for stat_name, value in item.items():
						if stat_name not in item_set:
							item_set[stat_name] = value
						elif stat_name in item_set and stat_name == 'Name':
							item_set[stat_name] = item_set[stat_name] + ' + ' + value
						else:
							item_set[stat_name] = float(item_set[stat_name]) + float(value)
				writer.writerow(item_set)

	def find_item_set(self, sets_file_name):
		with open(sets_file_name, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				if float(row['Poise']) >= 53 and float(row['Weight']) <= 22:
					print(row)