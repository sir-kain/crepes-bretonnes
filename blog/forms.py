__author__ = 'Waly'
from django import forms
from blog.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =('titre','auteur', 'contenu', 'slug', 'categorie')

class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
