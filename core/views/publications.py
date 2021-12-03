from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from core.models.files import File
from core.models.publications import Publication
from core.forms.publications import PublicationForm, PostForm
from django.db.models import Q


def publication_view(request, slug):
    publication = get_object_or_404(Publication, slug=slug, publish=True)
    files = File.objects.filter(publication=publication)

    if publication.type_publication.slug == 'post':
        template_name = 'core/post.html'
    else:
        template_name = 'core/publication.html'

    context = {
        'publication': publication,
        'files': files
    }
    return render(request, template_name, context)


def publication_search(request, template_name='core/results_search.html'):
    if request.method == 'POST':
        string_search = request.POST['search']

        qs = Publication.objects.filter(
            Q(title__icontains=string_search) |
            Q(author__full_name__icontains=string_search),
            Q(publish=True)
        ).distinct()[:16]

        context = {
            'term_search': string_search,
            'publications': qs
        }

        return render(request, template_name, context)
    else:
        return redirect('home-index')


def register_publication(request):
    form_publication = PublicationForm(request.POST or None)
    if request.method == 'POST':
        if form_publication.is_valid():
            publication = form_publication.save(commit=False)
            publication.save()

            messages.success(request, "Publicação cadastrada com sucesso!")
            return redirect('cadastrar-editar-perfil')
        else:
            messages.error(request, "Por favor, verifique os campos obrigatórios!")

    return render(request, 'core/register_publication.html', {'form': form_publication})


def register_post(request):
    form_post = PostForm(request.POST or None)
    if request.method == 'POST':
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.save()
            post.author.add(request.user.pk)

            messages.success(request, "Post cadastrado com sucesso!")
            return redirect('cadastrar-editar-perfil')
        else:
            messages.error(request, "Por favor, verifique os campos obrigatórios!")

    return render(request, 'core/register_post.html', {'form': form_post})

