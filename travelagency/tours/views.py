from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from tours.models import *
import requests
import json


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


# read
def index(request):
    tours = Tour.objects.all()
    return render(request, "index.html", {"tours": tours})


# create
def create(request):
    if request.method == "POST":
        tour = Tour()
        tour.title = request.POST.get("title")
        tour.cost = request.POST.get("cost")
        tour.description = request.POST.get("description")
        tour.save()
    return redirect('home')


# update
def edit(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)

        if request.method == "POST":
            tour.title = request.POST.get("title")
            tour.cost = request.POST.get("cost")
            tour.description = request.POST.get("description")
            tour.save()
            return redirect('home')
        else:
            return render(request, "edit.html", {"tours": tour})
    except Tour.DoesNotExist:
        return HttpResponseNotFound("<h2>Tour not found</h2>")


# delete
def delete(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)
        tour.delete()
        return redirect('home')
    except Tour.DoesNotExist:
        return HttpResponseNotFound("<h2>Tour not found</h2>")


def weather_api_test(request):
    appid = 'a2a6245cef875d740c11f8d31abacfb8'
    url = f'https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&lang=us&appid={appid}'
    response = requests.get(url)
    weatherdata = response.json()
    print("JSON Response :", weatherdata)
    return redirect('home')


def jokes(f):
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt


def jokes_api_test(request):
    f = r"https://official-joke-api.appspot.com/random_ten"
    a = jokes(f)
    for i in a:
        print(i["type"])
        print(i["setup"])
        print(i["punchline"], "\n")
    return redirect('home')
