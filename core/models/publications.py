import random
import uuid
import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from core.models.authors import Author
from core.models.categories import Category, Tag, Access, Knowledge, Type


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("publications", filename)


class Publication(models.Model):
    # general
    slug = models.SlugField('Slug', max_length=500, null=True, blank=True, unique=True)
    title = models.CharField('Título', max_length=500, null=False)
    subtitle = models.CharField('Sub-título', max_length=500, null=True, blank=True)

    # post
    content = RichTextUploadingField('Conteúdo', null=True, blank=True)
    excerpt = models.TextField(verbose_name='Excerto', null=True, blank=True)
    #image = models.ImageField('Imagem', upload_to=get_file_path, blank=True, null=True)

    # publications
    publish = models.BooleanField('Publicado?', null=False, default=False)
    resume = models.TextField('Resumo', blank=True, null=True)
    abstract = models.TextField('Abstract', blank=True, null=True)
    first_advisor = models.CharField('Primeiro orientador(a)', max_length=255, blank=True, null=False)
    second_advisor = models.CharField('Segundo orientador(a)', max_length=255, blank=True, null=False)
    keywords = models.CharField('Palavras-chave', max_length=255, blank=True, null=False)
    cnpq = models.CharField('CNPq', max_length=255, blank=True, null=True)
    language = models.CharField('Idioma', max_length=100, blank=True, null=True)
    country = models.CharField('Pais', max_length=100, blank=True, null=True, default='Brasil')
    editor = models.CharField('Editor', max_length=150, blank=True, null=True)
    initials_institution = models.CharField('Sigla instituição', max_length=150, blank=True, null=True)
    quote = models.TextField('Citação', blank=True, null=True)
    date_document = models.DateTimeField('Data do documento', blank=True, null=True)

    # relationship
    author = models.ManyToManyField(Author, verbose_name='Autor(es)', related_name='publication_author', blank=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='publication_categories',
                                        verbose_name='Categorias')
    knowledge_area = models.ForeignKey(Knowledge, blank=True, null=True, related_name='publication_knowledge',
                                       verbose_name='Área de conhecimento', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='publication_tag', verbose_name='Tags')
    type_publication = models.ForeignKey(Type, blank=True, null=True, related_name='publication_type',
                                         verbose_name='Tipo de publicação', on_delete=models.CASCADE)
    type_access = models.ForeignKey(Access, blank=True, null=True, related_name='publication_access',
                                    verbose_name='Tipo de acesso', on_delete=models.CASCADE)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}{str(random.randint(1000, 9999))}'
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
