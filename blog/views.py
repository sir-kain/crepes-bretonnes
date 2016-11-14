from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from blog.forms import ArticleForm, NouveauContactForm
from blog.models import Article, Contact
# Create your views here.

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def ajoutArticle(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = ArticleForm(request.POST)  # Nous reprenons les données

        #form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True
            return redirect('/blog/article/')

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ArticleForm()  # Nous créons un formulaire vide

    return render(request, 'blog/ajoutArticle.html', locals())

def modifArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':  # S'il s'agit d'une requête POST
       # form = ArticleForm(request.POST)  # Nous reprenons les données

        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer

            envoi = True


    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ArticleForm(instance=article)  # Nous créons un formulaire vide

    return render(request, 'blog/modifArticle.html', locals())

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})

@login_required
def liste(request):
    article = Article.objects.all()
    return render(request, 'blog/liste.html', {'articles':article})

def nouveau_contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True
    else:
        form = NouveauContactForm()

    return render(request, 'blog/contact.html', locals())

def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html', {'contacts': contacts})
