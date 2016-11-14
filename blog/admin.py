from django.contrib import admin

# Register your models here.
from blog.models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display= ('titre', 'auteur', 'date', 'categorie')
    list_filter= ('auteur','categorie',)
    date_hierarchy= 'date'
    ordering= ('date', )
    search_fields= ('titre', 'contenu')

"""
Le tableau a࠰iche les champs titre , auteur et date . Notez que les en-têtes sont nommés selon leur attribut verbose_name respectif.
Il est possible de filtrer selon les di࠰érents auteurs et la catégorie des articles (menu de droite).
L'ordre par défaut est la date de parution, dans l'ordre croissant (du plus ancien au plus récent).
Il est possible de chercher les articles contenant un mot, soit dans leur titre, soit dans leur contenu.
Enfin, il est possible de voir les articles publiés sur une certaine période (première ligne au-dessus du tableau).

"""

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)