from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
        context={
            "title": "Bienvenue!",
            "description": "Page d'accueil de notre application Django"
        }
    )
