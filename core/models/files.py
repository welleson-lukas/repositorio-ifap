import uuid
import os

from django.db import models
from core.models.publications import Publication


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("documents", filename)


class File(models.Model):
    title = models.CharField('Título', max_length=200)
    file = models.FileField(upload_to=get_file_path, null=True, verbose_name='Arquivo')
    created_at = models.DateTimeField('Created_at', auto_now_add=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Publicação', related_name='files')

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return self.title
