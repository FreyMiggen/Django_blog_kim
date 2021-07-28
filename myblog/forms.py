from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
	    model = Post
	    fields = ('title','author' ,'content', 'header_image')

	    widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
            
			
			'author': forms.TextInput(attrs={'value':'', 'id':'elder','type':'hidden'}),
			
			
			'content': forms.Textarea(attrs={'class': 'form-control'}),			
					
		}
  
    
        



	

		
                		
    		
	
	
	

    	
		