from django import forms
from blog_app.models import blog_post,UserProfile,Comment
from django.contrib.auth.models import User

class postForm(forms.ModelForm):
	#heading = forms.CharField(max_length = 128,help_text = "heading")
	#text  = forms. CharField(widget=forms.Textarea)
	class Meta:
		model = blog_post
		fields = ('heading','text')
class userForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','password') 

class userprofileForm(forms.ModelForm):
    class Meta:
        model = UserProfile		
        fields = ('email',)

class commentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ('comment',)        