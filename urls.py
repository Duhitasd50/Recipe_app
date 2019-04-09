from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('User', views.UserView)
router.register('Step', views.StepView)
router.register('Ingredient', views.IngredientView)
router.register('OurRecipe', views.OurRecipeView)


urlpatterns = [

    path('', include(router.urls))

]