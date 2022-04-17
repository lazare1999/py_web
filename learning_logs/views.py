from django.shortcuts import render

from .models import Topic


def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    t = Topic.objects.order_by('date_added')
    context = {'topics': t}
    return render(request, 'learning_logs/topics.html', context)
