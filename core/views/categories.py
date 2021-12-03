from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from core.models.publications import Publication
from core.models.categories import Category, Tag, Type, Knowledge, Access


def publications_per_categories(request, categoria):
    category_qs = get_object_or_404(Category, slug=categoria)
    publications = Publication.objects.filter(categories=category_qs, publish=True)

    context = {'category_info': category_qs, 'publications': publications}
    return render(request, 'core/category.html', context)


def publications_per_tag(request, tag):
    tag_qs = get_object_or_404(Tag, slug=tag)
    publications = Publication.objects.filter(tags=tag_qs, publish=True)

    context = {'category_info': tag_qs, 'publications': publications}
    return render(request, 'core/category.html', context)


def publications_per_type(request, tipo):
    type_qs = get_object_or_404(Type, slug=tipo)
    publications = Publication.objects.filter(type_publication=type_qs, publish=True)

    context = {'category_info': type_qs, 'publications': publications}
    return render(request, 'core/category.html', context)


def publications_per_knowledge(request, area):
    knowledge_qs = get_object_or_404(Knowledge, slug=area)
    publications = Publication.objects.filter(knowledge_area=knowledge_qs, publish=True)

    context = {'category_info': knowledge_qs, 'publications': publications}
    return render(request, 'core/category.html', context)


def publications_per_access(request, acesso):
    access_qs = get_object_or_404(Access, slug=acesso)
    publications = Publication.objects.filter(type_access=access_qs, publish=True)

    context = {'category_info': access_qs, 'publications': publications}
    return render(request, 'core/category.html', context)

