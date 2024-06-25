from django.apps import AppConfig


class ScholarshipsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'scholarships'

	# def ready(self):
	# 	import scholarships.signals  # Register the signals

	# # Ensure to initialize the __original_likes in your Scholarship model save method
	# def save(self, *args, **kwargs):
	# 	if self.pk:
	# 		self.__original_likes = Scholarship.objects.get(pk=self.pk).likes
	# 	else:
	# 		self.__original_likes = 0
	# 	super(Scholarship, self).save(*args, **kwargs)
