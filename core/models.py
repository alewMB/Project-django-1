from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class produitserveur(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitserveur , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitServeur", kwargs={"slug": self.slug})
    

    
class produitcamera(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='camera', null=True , blank=True)
    img2 = models.ImageField(upload_to='camera', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitcamera , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitCamera", kwargs={"slug": self.slug})


class produitcameraptz(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='camera', null=True , blank=True)
    img2 = models.ImageField(upload_to='camera', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitcameraptz , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitCameraptz", kwargs={"slug": self.slug})

class produitcamerabullet(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='camera', null=True , blank=True)
    img2 = models.ImageField(upload_to='camera', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitcamerabullet , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitCameraBullet", kwargs={"slug": self.slug})
# produit transmissions
class produitswitch(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='switch', null=True , blank=True)
    img2 = models.ImageField(upload_to='switch', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitswitch , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitswitch", kwargs={"slug": self.slug})

class produitroute(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='router', null=True , blank=True)
    img2 = models.ImageField(upload_to='router', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitroute , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitrouter", kwargs={"slug": self.slug})

class produitcable(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='cable', null=True , blank=True)
    img2 = models.ImageField(upload_to='cable', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitcable , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitcable", kwargs={"slug": self.slug})
# end produit transmissions
# produit telephone
class produitelephone(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='phone', null=True , blank=True)
    img2 = models.ImageField(upload_to='phone', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitelephone , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitTelephone", kwargs={"slug": self.slug})

class produitserveurappel(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='serveurappel', null=True , blank=True)
    img2 = models.ImageField(upload_to='serveurappel', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(produitserveurappel , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitserveurappel", kwargs={"slug": self.slug})

# end produit telephone

class formation(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(formation , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitFormation", kwargs={"slug": self.slug})


# Start services 
class ProduitService(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(ProduitService , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitService", kwargs={"slug": self.slug})

# Start ACTUALITÉ 
class ProduitActualite(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(ProduitActualite , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitActualite", kwargs={"slug": self.slug})

# Start À PROPOS 
class ProduitAPropos(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images', null=True , blank=True)
    detail = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(ProduitAPropos , self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("produitPropos", kwargs={"slug": self.slug})
