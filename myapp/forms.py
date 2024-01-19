from django import forms

class Choice(forms.Form):
    action = forms.ChoiceField(choices=[('coin', 'Coin'), ('dice', 'Dice'), ('random', 'Random')])
    tries = forms.IntegerField(min_value=1, max_value=64)
