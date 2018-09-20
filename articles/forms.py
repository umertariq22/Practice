from django import forms

class ArticleForm(forms.Form):
    classArr = {'class':'form-control'}
    title = forms.CharField(widget=forms.TextInput(attrs=classArr))
    author = forms.CharField(widget=forms.TextInput(attrs=classArr))
    article = forms.CharField(widget=forms.Textarea(attrs=classArr))
