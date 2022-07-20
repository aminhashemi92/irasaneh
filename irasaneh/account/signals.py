from .models import *
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from extensions.utils import send_wellcome_sms, send_request_resanehdar_sms, send_verify_resanehdar_sms

@receiver(post_save, sender=CustomUser)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Code.objects.create(user=instance)



@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, mphone=instance.phone)


    if created == False:
        profile = instance.profile
        profile.mphone =  instance.phone
        profile.save()
        # instance.save()
        # phone_number=instance.user
        # phone_number=instance.user.phone
        # print(phone_number)
        # send_wellcome(phone_number)


@receiver(pre_save, sender=Profile)
def profile_sms(sender, instance, *args, **kwargs):
    name = str(instance.firstname)
    if instance.firstname and instance.lastname:
        if not instance.is_completed:
            send_wellcome_sms(instance.mphone, name)
            instance.is_completed = True

    if instance.is_completed:
        pre = Profile.objects.get(id=instance.id)
        if pre.role != instance.role and instance.role == 'b':
            # print("resanehdar")
            send_verify_resanehdar_sms(instance.mphone, name)
