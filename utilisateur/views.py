from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from utilisateur.forms import ConnexionForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse


# Create your views here.

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            usernam = form.cleaned_data["username"]
            passwor = form.cleaned_data["password"]
            user = authenticate(username=usernam, password=passwor)  # Nous vérifions si les données sont correctes
            if user is not None:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                redirect('connexion.html')
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))