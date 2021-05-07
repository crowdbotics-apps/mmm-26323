from django.contrib import admin
from .models import (
    Category,
    Enrollment,
    SubscriptionType,
    Module,
    Group,
    Course,
    Subscription,
    Event,
    Recording,
)

admin.site.register(SubscriptionType)
admin.site.register(Subscription)
admin.site.register(Event)
admin.site.register(Group)
admin.site.register(Category)
admin.site.register(Recording)
admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(Module)

# Register your models here.
