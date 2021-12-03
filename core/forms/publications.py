from django import forms
from core.models.publications import Publication
from ckeditor_uploader.fields import RichTextUploadingField


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'subtitle', 'resume', 'abstract', 'first_advisor', 'second_advisor', 'keywords', 'cnpq',
                  'language', 'country', 'editor', 'initials_institution', 'quote', 'date_document', 'author',
                  'categories', 'knowledge_area', 'tags', 'type_publication', 'type_access']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control'}),
            'first_advisor': forms.TextInput(attrs={'class': 'form-control'}),
            'second_advisor': forms.TextInput(attrs={'class': 'form-control'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpq': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'editor': forms.TextInput(attrs={'class': 'form-control'}),
            'initials_institution': forms.TextInput(attrs={'class': 'form-control'}),
            'quote': forms.TextInput(attrs={'class': 'form-control'}),
            'date_document': forms.DateInput(attrs={'class': 'form-control'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'knowledge_area': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'type_publication': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'type_access': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'excerpt', 'categories', 'knowledge_area', 'tags', 'type_publication',
                  'type_access']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': RichTextUploadingField(),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'knowledge_area': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'type_publication': forms.Select(attrs={'class': 'form-select'}),
            'type_access': forms.Select(attrs={'class': 'form-select'}),
        }
