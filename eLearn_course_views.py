from django.contrib import messages
from django.shortcuts import render, redirect
from course.models import Domain, Course, CourseEnroll
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.
def is_course_enrolled(user, course):
    if CourseEnroll.objects.filter(user=user, course=course, status='E').exists():
        return True
    else:
        return False


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    if is_course_enrolled(request.user, course):
        return render(request, 'course/course_detail.html', {'course': course})
    else:
        return render(request, 'course/course_abstract.html', {'course': course})


def course_enroll(request, pk):
    course = Course.objects.get(id=pk)
    enroll = CourseEnroll(course=course, user=request.user)
    enroll.save()
    return redirect('course_detail', pk=pk)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")



def user_list(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'course/user_details.html', {'user': user})






