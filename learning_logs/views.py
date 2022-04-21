from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TopicForm, EntryForm, CarBrandForm, CarForm
from .models import Topic, Entry, CarBrands, Car
from django.urls import reverse


def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    t = Topic.objects.order_by('date_added')
    context = {'topics': t}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    t = Topic.objects.get(id=topic_id)
    entries = t.entry_set.order_by('-date_added')
    context = {'topic': t, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    t = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_e = form.save(commit=False)
            new_e.topic = t
            new_e.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': t, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    t = entry.topic
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[t.id]))
    context = {'entry': entry, 'topic': t, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def car_brands(request):
    """Show all topics."""
    t = CarBrands.objects.order_by('brand_foundation_date')
    context = {'brands': t}
    return render(request, 'learning_logs/brands.html', context)


def brand(request, brand_id):
    """Show a single topic and all its entries."""
    b = CarBrands.objects.get(id=brand_id)
    cars = b.car_set.order_by('-date_added')
    context = {'brand': b, 'cars': cars}
    return render(request, 'learning_logs/brand.html', context)


def new_brand(request):
    """Add a new brand."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CarBrandForm()
    else:
        # POST data submitted; process data.
        form = CarBrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:car_brands'))
    context = {'form': form}
    return render(request, 'learning_logs/new_brand.html', context)


def new_car(request, brand_id):
    """Add a new car for a particular brand."""
    b = CarBrands.objects.get(id=brand_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CarForm()
    else:
        # POST data submitted; process data.
        form = CarForm(data=request.POST)
        if form.is_valid():
            new_c = form.save(commit=False)
            new_c.brand = b
            new_c.save()
            return HttpResponseRedirect(reverse('learning_logs:brand', args=[brand_id]))
    context = {'brand': b, 'form': form}
    return render(request, 'learning_logs/new_car.html', context)


def edit_car(request, car_id):
    """Edit an existing car."""
    car = Car.objects.get(id=car_id)
    b = car.brand
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = CarForm(instance=car)
    else:
        # POST data submitted; process data.
        form = CarForm(instance=car, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:brand', args=[b.id]))
    context = {'car': car, 'brand': b, 'form': form}
    return render(request, 'learning_logs/edit_car.html', context)
