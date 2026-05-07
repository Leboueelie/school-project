from django.contrib import messages
from django.shortcuts import render


def contact(request):
    if request.method == "POST":
        messages.success(request, "Votre message a bien été envoyé. Merci !")
        return render(request, "contact/contact.html")
    return render(request, "contact/contact.html")
