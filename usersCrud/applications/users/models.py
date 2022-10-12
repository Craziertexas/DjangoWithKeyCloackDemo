from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.dispatch import receiver
import uuid
# Create your models here.
class Users(models.Model):
    DjangoUser = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    UUID = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)

@receiver(models.signals.pre_delete, sender=Users)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    try: instance.DjangoUser.delete()
    except: pass