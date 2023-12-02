from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm


def is_admin(user):
    return user.is_authenticated and user.is_staff


def index(request):
    cards = Card.objects.order_by('-id')
    return render(request, 'main/index.html', {'cards': cards})


def add(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("ДОСТУП ЗАПРЕЩЕН")
    form = CardForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'main/add.html', context)


def deleteCard(request, id):
    card = Card.objects.get(id=id)
    card.delete()
    return redirect('home')
