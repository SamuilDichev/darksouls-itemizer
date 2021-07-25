from src.itemizer import Itemizer


def main():
	itemizer = Itemizer(['Chest Armor Max Upgrade.csv', 'Gauntlets Max Upgrade.csv', 'Helms Max Upgrade.csv', 'Leg Armor Max Upgrade.csv'])
	itemizer.compute_and_save_all_possible_item_sets('sets')

if __name__ == "__main__":
	main()
