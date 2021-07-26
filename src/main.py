from src.itemizer import Itemizer


def main():
	itemizer = Itemizer(['Chest Armor Max Upgrade.csv', 'Gauntlets Max Upgrade.csv', 'Helms Max Upgrade.csv', 'Leg Armor Max Upgrade.csv'])
	itemizer.find_item_set('sets.csv')

if __name__ == "__main__":
	main()
