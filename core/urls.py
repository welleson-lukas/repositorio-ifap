from django.urls import path
from core.views.authors import *
from core.views.publications import *
from core.views.categories import *
from core.views.home_general import *


urlpatterns = [
    # HOME
    path('', home_view, name='home-index'),

    # AUTHOR
    path('autor/<autor>', profile_author_public, name='profile-author-public'),
    path('publicacao/<slug>', publication_view, name='view-publication'),

    # CATEGORIES
    path('categoria/<categoria>', publications_per_categories, name='publications-category'),
    path('tag/<tag>', publications_per_tag, name='publications-tag'),
    path('area-conhecimento/<area>', publications_per_knowledge, name='publications-knowledge'),
    path('tipo/<tipo>', publications_per_type, name='publications-type'),
    path('tipo-acesso/<acesso>', publications_per_access, name='publications-access'),


    path('busca', publication_search, name='route-testing'),

    # CRUD's
    path('registro/usuario/', register_user, name='create-user'),
    path('registro/perfil/', register_edit_profile, name='create-update-profile'),
    path('registro/publicacao/', register_publication, name='create-publication'),
    path('registro/post/', register_post, name='create-post'),
]
