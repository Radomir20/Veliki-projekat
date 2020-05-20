from django.db import models

class M_odjeca(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class M_obuca(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class M_oprema(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class Z_odjeca(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class Z_obuca(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class Z_oprema(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class D_odjeca(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class D_obuca(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv

class D_oprema(models.Model):
    naziv=models.CharField(max_length=1000)
    cijena=models.CharField(max_length=1000)
    slika=models.ImageField(null=True, blank=True)
    korpa = models.BooleanField(default=False)

    def __str__(self):
        return self.naziv