from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Step, Ingredient, OurRecipe
from .Serializer import UserSerializer, StepSerializer, IngredientSerializer, OurRecipeSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StepView(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class OurRecipeView(viewsets.ModelViewSet):
    queryset = OurRecipe.objects.all()
    serializer_class = OurRecipeSerializer