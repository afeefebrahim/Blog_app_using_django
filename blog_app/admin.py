from django.contrib import admin
from .models import blog_post,UserProfile,Comment
# Register your models here.

class postAdmin(admin.ModelAdmin):
	fields = ['name', 'text','heading']
	#prepopulated_fields = {'slug':('heading',)} 
class commentAdmin(admin.ModelAdmin):
    fields = ['comment','post']	
admin.site.register(blog_post, postAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment,commentAdmin)