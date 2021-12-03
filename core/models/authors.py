import uuid
import os
from PIL import Image
from django.utils.text import slugify
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("avatar", filename)


def qualify_name(fullname):
    name_list = fullname.split()
    last = f"{name_list[len(name_list) - 1].upper()}, "
    del (name_list[len(name_list) - 1])
    part = ' '.join(name_list)
    nome_qualificado = last + part
    return nome_qualificado


class Author(models.Model):
    image = models.ImageField('Avatar', upload_to=get_file_path, default='avatar.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authors')
    full_name = models.CharField('Nome Completo', max_length=255, null=True, blank=True)
    slug = models.SlugField('Slug', max_length=254, null=True, blank=True, unique=True)

    about = models.TextField('Sobre o Autor', max_length=500, null=True, blank=True)

    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    linkedin = models.CharField('Linkedin', max_length=255, null=True, blank=True)
    twitter = models.CharField('Twitter', max_length=255, null=True, blank=True)
    github = models.CharField('Github', max_length=255, null=True, blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    @staticmethod
    def resize_image(img, new_width=600):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.user.username)}'
            self.slug = slug

        if self.full_name:
            self.full_name = qualify_name(self.full_name)

        super().save(*args, **kwargs)

        max_image_size = 600

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.user.username
