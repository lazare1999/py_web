from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry, CarBrands, Car

admin.site.register(Topic)
admin.site.register(Entry)

admin.site.register(CarBrands)
admin.site.register(Car)
