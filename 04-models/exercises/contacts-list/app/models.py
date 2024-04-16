from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()

def create_contact(name, email,number,is_favorite):
    new_contact=Contact(name=name, email=email, phone=number,is_favorite=is_favorite )
    new_contact.save()
    return new_contact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(search_name):
    try:
        return Contact.objects.get(name = search_name)
    except:
        return None

def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(search_name, new_email):
    contact = Contact.objects.get(name = search_name)
    contact.email = new_email
    contact.save()

def delete_contact(search_name):
    contact = Contact.objects.get(name = search_name)
    contact.delete()
