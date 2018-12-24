# from django.db.models.signals import post_save
# from .models import batting,player_info
# from django.dispatch import receiver

# @receiver(post_save, sender=player_info)
# def create_batting(sender,  instance, created, **kwargs):
#     if created:
#         player_info.objects.create(player_id=instance)

# @receiver(post_save, sender=player_info)
# def save_batting(sender, instance, **kwargs):
#     instance.batting.save()
