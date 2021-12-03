from django.contrib import admin
from core.models.publications import Publication
from core.models.files import File
from core.models.categories import *
from core.models.authors import Author

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Knowledge)
admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(Access)
admin.site.register(Publication)
admin.site.register(File)
