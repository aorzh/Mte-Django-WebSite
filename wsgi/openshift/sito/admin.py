# Create your views here.
from django.contrib import admin
#from blog.models import Post
from sito.models import Image
from sito.models import Documento
from sito.models import Page
from sito.models import Caratteristiche
from sito.models import Benefici
from sito.models import Galleria
from sito.models import Allegato
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Page, MyModelAdmin)
#admin.site.register(Post)
admin.site.register(Image, MyModelAdmin)
admin.site.register(Documento, MyModelAdmin)
admin.site.register(Galleria, MyModelAdmin)
admin.site.register(Allegato, MyModelAdmin)
admin.site.register(Caratteristiche, MyModelAdmin)
admin.site.register(Benefici, MyModelAdmin)
