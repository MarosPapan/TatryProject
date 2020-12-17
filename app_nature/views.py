import requests
from django.shortcuts import render, redirect
from django .http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .decorators import unauthenticated_user, authenticated_user
from .models import peaks, mountain, texts_on_website, Profile, posts
from .forms import City_Form, UploadPost


#for i in tatras:
#    to_database(i)
#################################################################################################
#################################################################################################
def index(response):
    mountains = mountain.objects.all()
    nav = ''
    context = {'nav': nav, 'mt_all': mountains}
    return render(response, "app_nature/base.html", context)

def homepage(response):
    mountains = mountain.objects.all()
    main_text = texts_on_website.objects.get(id=1)
    description_of_tatras = texts_on_website.objects.get(id=2)
    nav = ''
    context = {'nav': nav,
               'maintext': main_text,
               'description_of_tatras': description_of_tatras,
               'mt_all': mountains}
    return render(response, "app_nature/homepage.html", context)

def all_peaks(response, mountain_id):
    all_mountains = mountain.objects.all()
    mountains = mountain.objects.get(pk=mountain_id)
    peaks_all = mountains.peaks_set.order_by('-height')
    context = {'mountains': mountains,
               'peaks_all': peaks_all,
               'mt_all': all_mountains}
    return render(response, "app_nature/peaks.html", context)

def detail(response, peak_id):
    peak = peaks.objects.get(pk=peak_id)
    all_mountains = mountain.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&cnt=16&units=metric&appid=5d4560bcfcabda5a9c36874498c9d0f0&lang=sk'
    city = 'Vysoke Tatry'

    err_msg = ''
    message = ''
    message_class = ''
    nav = 'bg-dark'
    if response.method == "GET":
        form = City_Form(response.GET)

        if form.is_valid():
            city_name = form.cleaned_data["name_of_city"]
            r = requests.get(url.format(city_name)).json()
            if r['cod'] == 200:
                city = city_name
            else:
                err_msg = 'The city does not exist'

            if err_msg:
                message = err_msg
                message_class = 'text-danger'

            else:
                message = 'City founded'
                message_class = 'text-success'
        else:
            city = 'Vysoke Tatry'

    else:
        form = City_Form()

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'min_temp': r['main']['temp_min'],
        'max_temp': r['main']['temp_max']
    }


    #print(city_weather)
    form = City_Form()
    context = {
        'peak': peak,
        'form': form,
        'city_weather': city_weather,
        'message': message,
        'message_class': message_class,
        'nav': nav,
        'mt_all': all_mountains
    }
    return render(response, "app_nature/detail.html", context)

@authenticated_user
def profilePage(response):
    user = response.user
    profile = Profile.objects.get(user=user)
    all_posts = profile.posts_set.order_by('-created_date')
    context = {'posts': all_posts, 'user': user}
    return render(response, "app_nature/profile.html", context)

@authenticated_user
def AddPost(response):
    user = response.user
    profile = Profile.objects.get(user=user)
    if response.method == "POST":
        form = UploadPost(response.POST)

        if form.is_valid():
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')

            new_post = posts(author=profile, image=image, description=description)
            new_post.save()
            return redirect("/profile")
    else:
        form = UploadPost()
        print('form is not valid')

    context = {"form": form}
    return render(response, "app_nature/add_post_page.html", context)
