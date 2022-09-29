import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
	
	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		if self.items is None:
			return None
		max_stock = self.items[0].stock
		max_stock_item = self.items[0]

		for item in self.items:
			if item.stock > max_stock:
				max_stock = item.stock
				max_stock_item = item
		return max_stock_item

		
			
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		if self.items is None:
			return None 
		max_price = self.items[0].price
		max_price_item = self.items[0]

		for item in self.items:
			if item.price > max_price:
				max_price = item.price
				max_price_item = item
		return max_price_item 
			
	


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		sentence = "Juno likes to eat bananas"
		self.assertEqual(count_a(sentence), 4)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		kroger = Warehouse()
		self.assertEqual(len(kroger.items), 0)
		kroger.add_item(self.item1)
		self.assertEqual(len(kroger.items), 1)
		print("pass")
		


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		kroger = Warehouse()
		kroger.add_item(self.item1)
		kroger.add_item(self.item2)
		kroger.add_item(self.item3)
		kroger.add_item(self.item4)
		kroger.add_item(self.item5)
		max_stock_name = kroger.get_max_stock()
		self.assertEqual(max_stock_name.name, self.item3.name)  #testing whether function returns Water from list of items


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		kroger = Warehouse()
		kroger.add_item(self.item1)
		kroger.add_item(self.item2)
		kroger.add_item(self.item3)
		kroger.add_item(self.item4)
		kroger.add_item(self.item5)
		max_price_name = kroger.get_max_price()
		self.assertEqual(max_price_name.name, self.item1.name)

		

def main():
	unittest.main()

if __name__ == "__main__":
	main()