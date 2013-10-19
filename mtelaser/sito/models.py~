from django.db import models
from tinymce import models as tinymce_models
from image_cropping import ImageRatioField, ImageCropField

class Image(models.Model):
    image_field = models.ImageField(upload_to='uploaded_images')

class Documento(models.Model):
    documento_allega = models.FileField(upload_to='uploaded_documenti')

# Pagina Prodotto
class Page(models.Model):
    titolo = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    cropping = ImageRatioField('image', '240x240')
    croppingslide = ImageRatioField('image', '1140x500')
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):
        return self.titolo

#Caratteristiche Tecniche
class Caratteristiche(models.Model):
    titolo = models.CharField(max_length=200)
    pagina = models.ForeignKey(Page, blank=True, null=True)
    laser = models.CharField(max_length=200, blank=True, null=True)
    raffreddamento = models.CharField(max_length=200, blank=True, null=True)
    assezy = models.CharField(max_length=200, blank=True, null=True)
    assez = models.CharField(max_length=200, blank=True, null=True)
    aspirazione = models.CharField(max_length=200, blank=True, null=True)
    motori = models.CharField(max_length=200, blank=True, null=True)
    assec = models.CharField(max_length=200, blank=True, null=True)
    alimentazione = models.CharField(max_length=200, blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):
        return self.titolo

#Benefici
class Benefici(models.Model):
    titolo = models.CharField(max_length=200)
    pagina = models.ForeignKey(Page)
    body = tinymce_models.HTMLField()
    pub_date = models.DateTimeField('date published')

    def __unicode__ (self):
        return self.titolo

# Galleria Prodotto
class Galleria(models.Model):
    gallerianome = models.CharField(max_length=200)
    pagina = models.ForeignKey(Page)
    image = models.ForeignKey(Image)
    cropping = ImageRatioField('image__image_field', '700x500')
    croppingthumb = ImageRatioField('image__image_field', '350x213')
    
    def __unicode__ (self):
        return unicode(self.gallerianome)

# PDF Documentazione ecc...
class Allegato(models.Model):
    allegatonome = models.CharField(max_length=200)
    pagina = models.ForeignKey(Page)
    documento = models.ForeignKey(Documento)
    
    def __unicode__ (self):
        return unicode(self.allegatonome)

