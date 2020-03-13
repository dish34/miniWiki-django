from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . forms import UserCreationForm

from bs4 import BeautifulSoup
from requests import get

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "scrap/login.html", {"mesage": None})
    context = {
        "user": request.user,
    }
    return render(request, "scrap/miniwiki.html", context)


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "scrap/login.html", {"message": "Invalid Crediential"})


def logout_view(request):
    logout(request)
    return render(request, "scrap/login.html", {"message": "Logged out"})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    form = UserCreationForm()
    return render(request, "scrap/signup.html", {"form": form})


def add_underscore(s):
    return s.replace(" ", "_")


def soup(request):
    # q = input("Wikipedia article: ")

    q = request.GET.get("your_title")
    if q:
        url_q = add_underscore(q)
        page = get("https://en.wikipedia.org/wiki/" + url_q)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find("h1", id="firstHeading").string
        print("title: " + title)
        table = soup.find("table")
        if not table:
            img = "No image available"
        else:
            img = table.find("img").get("src")
        body = soup.find("div", class_="mw-parser-output")
        if not body:
            # print("No text in this article")
            pall = "No text in this article"
            des = pall
        else:
            pall = body.find_all("p", limit=3)
            # print("description:", end=" ")
            des = []
            for p in pall:
                # print(p.get_text())
                des = p.get_text()

        # print("image url:" + img)
        context = {
            "test": "test",
            "title": title,
            "img": img,
            "des": des,
        }
    else:
        # print("nothing to disply")
        context = {
            "test": "test",
        }
    return render(request, "scrap/miniwiki.html", context)
