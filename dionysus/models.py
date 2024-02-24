from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
import random

# Create your models here.

@receiver(pre_delete, sender=User)
def reassign_vruoom_admin_id(sender, instance, **kwargs):
    clients = Client.objects.filter(vruoom_admin=instance)
    # Get all existing User ids
    existing_user_ids = set(User.objects.values_list('id', flat=True))
    
    for client in clients:
        # Generate a new random VruoomAdminId
        new_vruoom_admin_id = generate_new_vruoom_admin_id(existing_user_ids)
        client.vruoom_admin_id = new_vruoom_admin_id
        client.save()

def generate_new_vruoom_admin_id(existing_user_ids):
    # Generate a new random VruoomAdminId that does not exist in existing_user_ids
    new_id = random.randint(1, 999999)  # Adjust the range according to your needs
    while new_id in existing_user_ids:
        new_id = random.randint(1, 999999)
    return new_id

class Client(models.Model):
    businessName = models.CharField(max_length=100)
    vruoomAdminId = models.ForeignKey(User,on_delete=models.PROTECT)
    address = models.CharField(max_length=100)
    GSTIN = models.CharField(max_length=100)
    SAPCode = models.CharField(max_length=100)
    PAN = models.CharField(max_length=100)
    YearOfEstablishment = models.DateField()
    TypeOfFirm = models.CharField(max_length=100)
    TypeOfSite = models.CharField(max_length=100)

    def __str__(self):
        return self.businessName





