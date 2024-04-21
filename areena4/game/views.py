from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Race, Gladiator, Team
from .serializers import GladiatorSerializer


def api(request):
    # logic for game API
    # retrieve data from db and return as JSON

    active_gladiator = Gladiator.objects.filter(team__name="Player Team").first()

    # Check if a gladiator was found
    if active_gladiator:
        # If a gladiator was found, construct the response data

        serializer = GladiatorSerializer(active_gladiator)
        return JsonResponse(serializer.data)
    else:
        # If no gladiator was found, return an error response
        return JsonResponse(
            {'error': 'No active gladiator found for the Player team'}, status=404)

def get(self, request):
    gladiator = Gladiator.objects.filter(team__name='Player Team').first()
    serializer = GladiatorSerializer(gladiator)
    return Response(serializer.data, status=status.HTTP_200_OK)

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