from django import forms
from django.core.validators import *
from django.db import models
from .Schedule import Schedule

class UserForm(forms.Form):
    number = forms.CharField(max_length=12)
    sex= forms.ChoiceField(choices = ( 
    ("M", "MEN"), 
    ("F", "WOMEN")
))
    day= forms.IntegerField(max_value=31,min_value=1,error_messages={'required': 'Введите свою дату рождения ниже:'})
    month = forms.ChoiceField(choices = ( 
    ("1", "Январь"), 
    ("2", "Февраль"),
    ("3", "Март"),
    ("4", "Апрель"),
    ("5", "Май"),
    ("6", "Июнь"),
    ("7", "Июль"),
    ("8", "Август"),
    ("9", "Сентябрь"),
    ("10", "Октябрь"),
    ("11", "Ноябрь"),
    ("12", "Декабрь"),
))
    year= forms.IntegerField(max_value=2020,min_value=1900)
    
class SignIn(forms.Form):
    number = forms.CharField(max_length=12)



class RoomChange(forms.Form):
    room = forms.ChoiceField(choices = ((None,None),('109','109')))
    

class DayChange(forms.Form):
    dayChange = forms.ChoiceField(choices=(('Понедельник','Понедельник'),('Вторник','Вторник'),("Среда","Среда")))


class signUp(forms.Form):
    ch = Schedule.getFreeTime()
    signup = forms.ChoiceField(choices = ch)
    

    
