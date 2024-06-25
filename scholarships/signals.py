# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Scholarship
# from accounts.models import Scholar_liked  # Import Scholar_liked from the appropriate app

# @receiver(post_save, sender=Scholarship)
# def create_scholar_liked(sender, instance, created, **kwargs):
#     if not created:  # Only run this when an existing instance is updated
#         # Assuming you have a way to get the user who liked the scholarship
#         # user = get_current_user()  # Implement this function based on your logic

#         # Check if the 'likes' field was incremented
#         if instance.likes > instance.__original_likes:
#             Scholar_liked.objects.create(
#                 # user=user,
#                 liked_scholarship=instance.name,
#                 liked_scholarship_slug=instance.slug,
#             )

#         # Update the original likes value
#         instance.__original_likes = instance.likes