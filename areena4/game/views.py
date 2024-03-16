from django.shortcuts import render, redirect
from .models import Race, Gladiator, Team

# from .serializers import GladiatorSerializer


def redirect_to_game(request):
    return redirect('game/')

def gladiator_detail(request):
    # Query the first 8 gladiators from the database
    gladiators = Gladiator.objects.all()[:8]
    return render(request, 'gladiator_detail.html', {'gladiators': gladiators})


def base(request):
    return render(request, 'base.html')


def arena_matrix(request):
    # Initialize the arena matrix
    arena = [[None for _ in range(8)] for _ in range(8)]

    # Get the gladiator with id=1
    gladiator = Gladiator.objects.get(id=1)

    # Place the gladiator at position (2, 1) in the arena
    x = 2
    y = 1
    arena[y][x] = gladiator

    # Pass the arena to the template
    return render(request, 'gladiator_detail.html', {'arena': arena})