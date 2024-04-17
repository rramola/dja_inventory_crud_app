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


def filter_items(x, y):
    try:
        item = Inventory.objects.filter(**{x: y})
        print(item[0].id)
        return item
    except:
        return None
