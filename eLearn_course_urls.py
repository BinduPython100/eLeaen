from django.urls import path
from . import views

urlpatterns = [
    path('course_detail/<int:pk>', views.course_detail, name='course_detail'),
    path('course_enroll/<int:pk>', views.course_enroll, name='course_enroll'),
    path("logout", views.logout_request, name="logout"),
     path('users/<int:pk>', views.user_list, name='users')
]
