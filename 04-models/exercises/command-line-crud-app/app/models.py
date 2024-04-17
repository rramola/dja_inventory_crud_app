from django.db import models

# Create your models here.


class Inventory(models.Model):
    brand = models.TextField()
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    identifier = models.TextField()


def create_item(brand, name, description, quantity, price, identifier):
    new_item = Inventory(
        brand=brand,
        name=name,
        description=description,
        quantity=quantity,
        price=price,
        identifier=identifier,
    )
    new_item.save()
    return new_item


def all_items():
    return Inventory.objects.all()


def filter_items(key, value):
    # INSTEAD OF CREATING INDIVIDUAL FUNCTIONS TO SEARCH THROUGH SPECIFIC OBJECT PROPERTIES
    # ONE FUNCTION IS USED THAT CAN SEARCH BASED ON WHATEVER PROPERTY NAME AND PROPERTY VALUE IS PASSED TO IT
    # THIS IS DONE BY UNPACKING THE KEY, VALUE PAIR INTO A KEYWORD ARGUMENT USING **
    # THE FUNCTION NOW USES Inventory.objects.filter(key=value)
    # INSTEAD OF USING Inventory.objects.get(name = "battery")
    # THIS ALLOWS THE SEARCH TO BE MORE FLEXIBLE 

    try:
        item = Inventory.objects.filter(**{key:value})
        return item
    except:
        return None
