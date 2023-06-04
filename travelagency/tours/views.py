from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.template.backends import django

from tours.models import *


class Image:
    small_image = ''
    large_image = ''

    def __init__(self, small_image, large_image):
        self.small_image = small_image
        self.large_image = large_image


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>{year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found or not implemented</h1>")


def main_page(request):
    main_category = 'Hot Tours'
    categories = Category.objects.order_by("-name")
    tours = Tour.objects.filter(category__name=main_category)
    gallery = [Image(small_image='tours/images/gallery-image-1-270x195.jpg', large_image='tours/images/gallery-image-1-1200x800-original.jpg'),
               Image(small_image='tours/images/gallery-image-2-270x195.jpg', large_image='tours/images/gallery-image-2-1200x800-original.jpg'),
               Image(small_image='tours/images/gallery-image-3-270x195.jpg', large_image='tours/images/gallery-image-3-1200x800-original.jpg'),
               Image(small_image='tours/images/gallery-image-4-270x195.jpg', large_image='tours/images/gallery-image-4-1200x800-original.jpg'),
               Image(small_image='tours/images/gallery-image-5-270x195.jpg', large_image='tours/images/gallery-image-5-1200x800-original.jpg'),
               Image(small_image='tours/images/gallery-image-6-270x195.jpg', large_image='tours/images/gallery-image-6-1200x800-original.jpg')]
    context = {
        'categories': categories,
        'main_category': main_category,
        'tours': tours,
        'images': gallery
    }
    return render(request, 'tours/main_page.html', context=context)


def show_post(request, tour_category):
    categories = Category.objects.order_by("-name")
    tours = Tour.objects.filter(category__slugify_name=tour_category)
    category = Category.objects.get(slugify_name=tour_category)
    gallery = [Image(small_image=f'tours/images/{category.name}/rsz_picture-1200-x-800-1.jpg', large_image=f'tours/images/{category.name}/picture-1200-x-800-1.jpg'),
               Image(small_image=f'tours/images/{category.name}/rsz_picture-1200-x-800-2.jpg', large_image=f'tours/images/{category.name}/picture-1200-x-800-2.jpg'),
               Image(small_image=f'tours/images/{category.name}/rsz_picture-1200-x-800-3.jpg', large_image=f'tours/images/{category.name}/picture-1200-x-800-3.jpg'),
               Image(small_image=f'tours/images/{category.name}/rsz_picture-1200-x-800-4.jpg', large_image=f'tours/images/{category.name}/picture-1200-x-800-4.jpg'),
               Image(small_image=f'tours/images/{category.name}/rsz_picture-1200-x-800-5.jpg', large_image=f'tours/images/{category.name}/picture-1200-x-800-5.jpg'),
               Image(small_image=f'tours/images/{category.name}/rsz_picture-1200-x-800-6.jpg', large_image=f'tours/images/{category.name}/picture-1200-x-800-6.jpg')]
    context = {
        'tours': tours,
        'title': category.name,
        'categories': categories,
        'selected_category': category.name,
        'images': gallery
    }
    return render(request, 'tours/category_page.html', context=context)


def logout_func(request):
    logout(request)
    return redirect('home')
