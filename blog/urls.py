__author__ = 'Waly'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home, name='home'),
    url(r'^date$', views.date_actuelle, name='date_actuelle'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition, name='addition'),
    url(r'^ajoutArticle/$', views.ajoutArticle, name='ajoutArticle'),
    url(r'^modifArticle/(?P<id>\d+)/$', views.modifArticle, name='modifArticle'),
    url(r'^article/(?P<id>\d+)$', views.lire),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', views.lire, name='lire'),
    url(r'^article/$', views.liste, name='liste'),
    url(r'^ajoutContact/$', views.nouveau_contact, name='ajoutContact'),
    url(r'^contacts/$', views.voir_contacts, name='les_contacts'),

]
