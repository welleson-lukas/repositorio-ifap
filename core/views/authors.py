from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from core.models.authors import Author
from core.models.publications import Publication
from core.forms.authors import AuthorForm, RegisterUserForm, UserForm


def profile_author_public(request, autor):
    profile_qs = get_object_or_404(Author, slug=autor)
    publications = Publication.objects.filter(author=profile_qs, publish=True)

    context = {'author': profile_qs, 'publications': publications}
    return render(request, 'core/profile.html', context)


def register_user(request):
    form = RegisterUserForm(request.POST or None)

    if request.method == "POST":
        password_confirm = request.POST['password_confirm']
        password = request.POST['password']

        if password == password_confirm:
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(user.password)
                user.is_active = True
                user.save()

                messages.success(request, "Cadastrado com sucesso!")
                return redirect('cadastrar-editar-perfil')
            else:
                messages.error(request, "Por favor, verifique os campos obrigatórios!")
        else:
            messages.error(request, "Senhas não conferem. Tente novamente!")

    return render(request, 'core/register_user.html', {'form': form})


def register_edit_profile(request):
    user_qs = get_object_or_404(User, pk=request.user.pk)
    author_qs = get_object_or_404(Author, pk=request.user.pk)

    form_user = UserForm(request.POST, instance=user_qs)
    form_author = AuthorForm(request.POST, request.FILES, instance=author_qs)

    if request.method == 'POST':

        if form_user.is_valid():
            if form_author.is_valid():
                user = form_user.save(commit=False)
                user.save()

                author = form_author.save(commit=False)
                author.full_name = f'{user.first_name} {user.last_name}'
                author.save()

                messages.success(request, "Perfil atualizado com sucesso!")
                return redirect('login')
            else:
                messages.error(request, "Por favor, verifique os campos obrigatórios!")
        else:
            messages.error(request, "Por favor, verifique os campos obrigatórios!")
    else:
        form_user = UserForm(instance=user_qs)
        form_author = AuthorForm(instance=author_qs)

    return render(request, 'core/register_profile.html', {'form_user': form_user, 'form_author': form_author})
