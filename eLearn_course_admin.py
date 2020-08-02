from django.contrib import admin
from .models import Domain, Course, Video, CourseEnroll, Material, Lesson


# Register your models here.

class LessonMaterialInline(admin.TabularInline):
    model = Material
    extra = 0


class LessonInline(admin.TabularInline):
    model = Lesson
    fields = ('name', 'changeformlink')
    readonly_fields = ('changeformlink',)
    extra = 0


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    search_fields = ('name', 'course__title')
    list_display = ('name', 'course')
    list_filter = ('course',)
    inlines = [LessonMaterialInline,VideoInline]


admin.site.register(Domain)
# admin.site.register(Course)
# admin.site.register(Video)
admin.site.register(CourseEnroll)
# admin.site.register(Material)
# admin.site.register(Lesson)
