# from django.urls import path
# from .views import (
#     student_ListCreate,
#     StudentView,
#     StudentListCreate,
#     StudenMixinView
# )
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet

# router = DefaultRouter()
# router.register(r'students', StudentViewSet, basename='student')

# urlpatterns = [
#     path('students/fbv/', student_ListCreate),
#     path('students/apiview/', StudentView.as_view()),
#     path('students/generic/', StudentListCreate.as_view()),
#     path('students/mixin/', StudenMixinView.as_view()),
#     path('', include(router.urls)),
# ]
