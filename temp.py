'''


Design an inventory management system for a storage facility with multiple numbered spots.
Each spot can store an item, and each item has a unique item ID.
The inventory management system should support the following operations:

 - Check if an item is available in the inventory.
 - Check if a spot is available to store an item.
 - Add a new item to the inventory and specify a spot number
 - Remove an item from the inventory
 - Get the spot number for a given item ID.

Provide an implementation for this inventory management system.
'''

'''
1. kind of a mapping fo item and spot - dictionary
2. 
'''



class InventoryManagement():

    def __init__(self, total_spots):
        self.total_spots = total_spots # total initial spots
        # dictionary mapping for item to spot
        # ID -> number
        self.item_to_spot = {}
        self.spot_to_item = {}

    def is_item_available(self, item_id):
        if self.item_to_spot[item_id]:
            return True
        return False
        # return item_id in self.item_to_spot

    def is_spot_available(self, spot_number):
        if self.spot_to_item[spot_number]:
            return True
        return False
        # return spot_number is self.spot_to_item

    def add_item(self, item_number, spot_number):
        if spot_number > self.total_spots:
            print(f"Spot number {spot_number} not available")

        if self.is_item_available(item_number):
            print(f"Item number {item_number} already available")

        if not self.is_spot_available(spot_number):
            print(f"Spot number {spot_number} is already taken")

        self.spot_to_item[spot_number] = item_number
        self.item_to_spot[item_number] = spot_number
        print(f"Item stored at Spot number {spot_number} not available")

    def remove_item(self, item_number):
        if not self.is_item_available(item_number):
            print(f"Item {item_number} does not exist")

        spot_number = self.item_to_spot[item_number]
        del self.spot_to_item[spot_number]
        del self.item_to_spot[item_number]
        print(f"Remove")

    def get_spot_number(self, item_number):
        if not self.is_item_available(item_number):
            print(f"Item {item_number} does not exist")

        spot_number = self.item_to_spot[item_number]
        print(f"Spot number {spot_number}")
        return spot_number






