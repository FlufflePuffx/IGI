from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, default='')
    photo = models.ImageField(upload_to="photos/%Y")
    cost = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="time of creation")
    time_update = models.DateTimeField(auto_now=True, verbose_name="last update")
    country = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.OneToOneField('Hotel', on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField('Category', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['cost']


class Country(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)
    weather = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']


class Hotel(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True)
    rating = models.IntegerField(default=0, verbose_name="rating (stars)")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def stars(self):
        return str(self.rating)


class Client(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    tel_number = models.CharField(max_length=20, verbose_name="telephone number")
    ticket = models.ManyToManyField('Ticket', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, default='')
    slugify_name = models.CharField(max_length=200, db_index=True, default=slugify(name))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"category/{self.slugify_name}/"

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Ticket(models.Model):
    departure_date = models.DateTimeField(null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    term = models.ForeignKey('Term', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.tour.title} - term: {self.term} - departure date: {self.departure_date}"


class Term(models.Model):
    days = models.IntegerField(default=7)

    def __str__(self):
        return f"{self.days} days"
