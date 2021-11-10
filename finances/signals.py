from .models import Payment_record, Payment
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Payment)
def create_payment_record(sender, instance, created, **kwargs):
    # print('Am good')
    if created:
        Payment_record.objects.create(student_name=instance)

# post_save.connect(create_payment_record, sender=Payment)

@receiver(post_save, sender=Payment)
def save_payment_record(sender, instance, **kwargs):
    instance.Payment_record.save






# post_save.connect(create_payment_record, sender=Payment)

# def update_payment_record(instance, created, **kwargs):
#     if created == False:
#         instance.Student_payment_record.save()

# post_save.connect(update_payment_record, sender=Payment)
