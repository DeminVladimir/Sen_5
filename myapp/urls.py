from django.urls import path
from .views import flip_coin, roll_dice, generate_random_number, choice_rand

urlpatterns = [
    path('coin', flip_coin, name='Coin'),
    path('dice', roll_dice, name='Dice'),
    path('num', generate_random_number, name='Num'),
    path('', choice_rand, name='choice_rand'),
]
