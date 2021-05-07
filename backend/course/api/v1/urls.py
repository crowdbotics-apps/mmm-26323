from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    LessonViewSet,
    EnrollmentViewSet,
    SubscriptionTypeViewSet,
    PaymentMethodViewSet,
    ModuleViewSet,
    GroupViewSet,
    CourseViewSet,
    SubscriptionViewSet,
    EventViewSet,
    RecordingViewSet,
)

router = DefaultRouter()
router.register("lesson", LessonViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("event", EventViewSet)
router.register("group", GroupViewSet)
router.register("category", CategoryViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("recording", RecordingViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("course", CourseViewSet)
router.register("module", ModuleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
