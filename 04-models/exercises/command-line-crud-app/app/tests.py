from django.test import TestCase
from app import models



class TestInventory(TestCase):
    def test_can_create_inventory_item(self):
        item = models.create_item(
            "Uniroyal",
            "Tiger Paw Touring A/S",
            "Tru-Last Technology gives you long, even treadwear by managing stress within the tire footprint. Our Broadest Product Line Ever.",
            10,
            98,
            "Tires", 
        )

        self.assertEqual(item.brand, "Uniroyal")
        self.assertEqual(item.name, "Tiger Paw Touring A/S")
        self.assertEqual(item.description, "Tru-Last Technology gives you long, even treadwear by managing stress within the tire footprint. Our Broadest Product Line Ever.")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.price, 98)
        self.assertEqual(item.identifier, "Tires")

    def test_can_view_all_items(self):
        inventory_data = [
            {
                    "brand": "Uniroyal",
                    "name": "Tiger Paw Touring A/S",
                    "description": "Tru-Last Technology gives you long, even treadwear by managing stress within the tire footprint. Our Broadest Product Line Ever.",
                    "quantity": 10,
                    "price": 98,
                    "identifier": "Tires", 
            },
            {
                    "brand": "Michelin",
                    "name": "Defender2",
                    "description": "The Defender2 is Michelin's Standard Touring All-Season tire built for drivers of coupes, sedans, crossover, SUVs and minivans, looking for a dependable tire with reliable year-round traction.",
                    "quantity":8,
                    "price": 166,
                    "identifier": "Tires", 
            },
            {
                    "brand": "Duralast Gold",
                    "name": "Ceramic Brake Pads",
                    "description": "Eliminate brake noise and restore your vehicles original stopping power with Duralast Gold Brake Pads.",
                    "quantity": 3,
                    "price": 29,
                    "identifier": "Brakes", 
            },
            {
                    "brand": "Continental",
                    "name": "Serpentine Belt",
                    "description": "Install this belt with complete confidence to keep your vehicle on the road and to help restore original equipment performance.",
                    "quantity": 5,
                    "price": 52,
                    "identifier": "Belts", 
            },
            {
                    "brand": "Duralast Gold",
                    "name": "H6",
                    "description": "Duralast Gold Automotive Batteries are backed by a 3-year, free replacement, nationwide warranty.",
                    "quantity": 1,
                    "price": 215,
                    "identifier": "Batteries", 
            },
            {
                    "brand": "Econocraft",
                    "name": "H6",
                    "description": "Delivers ample cranking power for sure starts",
                    "quantity": 1,
                    "price": 89,
                    "identifier": "Batteries", 
            },
            {
                    "brand": "STP",
                    "name": "SA10262",
                    "description": "STP Air Filters come from one of the world’s most recognized automotive aftermarket brands.",
                    "quantity": 4,
                    "price": 20,
                    "identifier": "Filters", 
            },
        ]

        for item in inventory_data:
            models.create_item(
                item["brand"],
                item["name"],
                item["description"],
                item["quantity"],
                item["price"],
                item["identifier"],
            )

        inventory_items = models.all_items()
        self.assertEqual(len(inventory_items), len(inventory_data))
        
        sort_inventory_from_inventory_data_by_name = sorted(inventory_data, key=lambda i: i["name"])
        sort_inventory_from_inventory_items_by_name = sorted(inventory_items, key=lambda i: i.name)

        for data, item in zip(sort_inventory_from_inventory_data_by_name, sort_inventory_from_inventory_items_by_name):
            self.assertEqual(data["brand"], item.brand)
            self.assertEqual(data["name"], item.name)
            self.assertEqual(data["description"], item.description)
            self.assertEqual(data["quantity"], item.quantity)
            self.assertEqual(data["price"], item.price)
            self.assertEqual(data["identifier"], item.identifier)
    
    def test_sort_inventory_by_attribute_and_name(self):
        inventory_data = [
            {
                    "brand": "Uniroyal",
                    "name": "Tiger Paw Touring A/S",
                    "description": "Tru-Last Technology gives you long, even treadwear by managing stress within the tire footprint. Our Broadest Product Line Ever.",
                    "quantity": 10,
                    "price": 98,
                    "identifier": "Tires", 
            },
            {
                    "brand": "Michelin",
                    "name": "Defender2",
                    "description": "The Defender2 is Michelin's Standard Touring All-Season tire built for drivers of coupes, sedans, crossover, SUVs and minivans, looking for a dependable tire with reliable year-round traction.",
                    "quantity":8,
                    "price": 166,
                    "identifier": "Tires", 
            },
            {
                    "brand": "Duralast Gold",
                    "name": "Ceramic Brake Pads",
                    "description": "Eliminate brake noise and restore your vehicles original stopping power with Duralast Gold Brake Pads.",
                    "quantity": 3,
                    "price": 29,
                    "identifier": "Brakes", 
            },
            {
                    "brand": "Continental",
                    "name": "Serpentine Belt",
                    "description": "Install this belt with complete confidence to keep your vehicle on the road and to help restore original equipment performance.",
                    "quantity": 5,
                    "price": 52,
                    "identifier": "Belts", 
            },
            {
                    "brand": "Duralast Gold",
                    "name": "H6",
                    "description": "Duralast Gold Automotive Batteries are backed by a 3-year, free replacement, nationwide warranty.",
                    "quantity": 1,
                    "price": 215,
                    "identifier": "Batteries", 
            },
            {
                    "brand": "Econocraft",
                    "name": "H6",
                    "description": "Delivers ample cranking power for sure starts",
                    "quantity": 1,
                    "price": 89,
                    "identifier": "Batteries", 
            },
            {
                    "brand": "STP",
                    "name": "SA10262",
                    "description": "STP Air Filters come from one of the world’s most recognized automotive aftermarket brands.",
                    "quantity": 4,
                    "price": 20,
                    "identifier": "Filters", 
            },
        ]

        for item in inventory_data:
            models.create_item(
                item["brand"],
                item["name"],
                item["description"],
                item["quantity"],
                item["price"],
                item["identifier"],
            )
        
        item_attribute_found_search_dict = {
            # "brand": "STP",
            # "name": "H6",
            # "quantity": 5,
            # "price": 98,
            # "brand": "Duralast Gold",
            "identifier": "Tires", 
            # "sdfhsadf": "dsfgkj"           
        }

        find_items = models.filter_items(item_attribute_found_search_dict)
        print (find_items)