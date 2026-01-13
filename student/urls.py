from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns =[
    # url for @api_view
    path('students/', student_ListCreate()),

    # url for APIView
    path('students/', StudentView.as_view()),

    # url for Generic view
    path('students/', StudentListCreate.as_view()),

    # url for mixin view
    path('students/', StudenMixinView.as_view()),

    # url for Viewset
    router = DefaultRouter()
    router.register('students', StudentViewSet)
    urlpatterns=router.urls
]