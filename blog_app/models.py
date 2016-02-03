from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class blog_post(models.Model):
	name = models.CharField(max_length=100)
	heading = models.CharField(max_length=100)
	text = models.TextField()
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.heading)
		super(blog_post, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.heading            
	def __str__(self):
		return self.heading

class Comment(models.Model):
    post = models.ForeignKey(blog_post)
    comment = models.CharField(max_length=100)
    def __str__(self):
        return self.comment
    def __unicode__(self):
		return self.comment      
class UserProfile(models.Model):
    user = models.OneToOneField(User)      
    email = models.EmailField(blank=True)
    #def __unicode__(self):
    #    return self.user.username 