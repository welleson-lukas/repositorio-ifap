from django.shortcuts import render
from core.models.publications import Publication


def home_view(request, template_name='core/home.html'):
    publications_qs = Publication.objects.filter(
        publish=True
    )[:16]

    context = {
        'publications': publications_qs
    }

    return render(request, template_name, context)
