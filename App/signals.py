from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

# LOCAL IMPORTS
from .models import Reviewer, Brand

@receiver(post_save, sender=User)
def createReviewerProfile(sender, instance, created,request, **kwargs):
    if created:
        Reviewer.objects.create(user=instance)
        print('User profile created')

@receiver(post_save, sender=User)
def saveReviewerProfile(sender, instance, created, **kwargs):
    instance.reviewer.save()
    print('profile saved')

@receiver(post_save, sender=User)
def createBrandProfile(sender, instance, created, request, **kwargs):
    if created:
        Brand.objects.create(user=instance)
        group = Group.objects.get(name='Brand')
        sender.groups.add(group)
        request.groups.add(group)
        print('User profile created')

@receiver(post_save, sender=User)
def saveBrandProfile(sender, instance, created, **kwargs):
    instance.brand.save()
    print('profile saved')
