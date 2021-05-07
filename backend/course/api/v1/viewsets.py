from rest_framework import authentication
from course.models import (
    Category,
    Lesson,
    Enrollment,
    SubscriptionType,
    PaymentMethod,
    Module,
    Group,
    Course,
    Subscription,
    Event,
    Recording,
)
from .serializers import (
    CategorySerializer,
    LessonSerializer,
    EnrollmentSerializer,
    SubscriptionTypeSerializer,
    PaymentMethodSerializer,
    ModuleSerializer,
    GroupSerializer,
    CourseSerializer,
    SubscriptionSerializer,
    EventSerializer,
    RecordingSerializer,
)
from rest_framework import viewsets


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Lesson.objects.all()


class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionTypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = SubscriptionType.objects.all()


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscription.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Event.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Group.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class RecordingViewSet(viewsets.ModelViewSet):
    serializer_class = RecordingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Recording.objects.all()


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Enrollment.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Course.objects.all()


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Module.objects.all()
