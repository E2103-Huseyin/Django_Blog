from django import forms
from .models import Post, Comment,Category

class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(queryset=category)
    class Meta:
        model = Post
        fields = (
            "title" ,
            "content" ,
            "image" ,
            "category",
            "status" , 
            
        )
        