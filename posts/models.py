from django.db import models
from time import  time
# Create your models here.
def get_filename(instance, filename):
	return "uploads/%s_%s" % (str(time()).replace('.','_'), filename)


class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length = 140)
	body = models.TextField()
	thumbnail = models.FileField(upload_to=get_filename)
	date = models.DateTimeField(auto_now_add=True)
	user_id = models.IntegerField()


	def __unicode__(self):
		return self.title
		

