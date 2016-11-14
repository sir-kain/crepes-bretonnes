__author__ = 'Waly'
from django.conf.urls import url
from . import views
# On import les vues de Django, avec un nom spécifique
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^connexions$', auth_views.login, {'template_name': 'connexion.html'}),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
]
