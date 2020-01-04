from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class MEta:
        model = Post
        fields = "__all__"
