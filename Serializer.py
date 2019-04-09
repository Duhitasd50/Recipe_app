from rest_framework import serializers
from .models import User, Step, Ingredient, OurRecipe


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id','username', 'firstname', 'lastname', 'email', 'password')


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('url','id','step_text')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('url','id','ingredient')


class OurRecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OurRecipe
        fields = ('url','id','recipe_name', 'user', 'ingredient', 'step')
