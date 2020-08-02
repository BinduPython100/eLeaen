from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render
from .models import District, Student, Teacher
from course.models import Domain, Course, CourseEnroll
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    courses = Course.objects.filter(is_active=True).annotate(num_enrollment=Count('courseenroll')).order_by(
        '-num_enrollment')
    return render(request, 'lms/index.html', {'courses': courses})


class CustomLoginView(LoginView):
    redirect_authenticated_user = True


def user_request(request):
    return render(request, 'course/profile.html')


# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         post = User.objects.filter(username=username)
#         if post:
#             username = request.POST['username']
#             request.session['username'] = username
#             return redirect("course/user_details")
#         else:
#             return render(request, 'lms/index.html', {})
#     return render(request, 'lms/index.html', {})