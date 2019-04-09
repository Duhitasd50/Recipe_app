from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname


class Step(models.Model):
    step_text = models.CharField(max_length=200)

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=20)

    def __str__(self):
        return self.ingredient


class OurRecipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    step = models.ForeignKey(
        Step,
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.recipe_name, self.ingredient, self.step, self.user
