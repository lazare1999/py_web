from django import forms
from .models import Topic, Entry, CarBrands, Car


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrands
        fields = ['description']
        labels = {'description': ''}


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 90})}
