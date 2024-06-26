from django.contrib import admin

from .models import Stage, Exam, ExamModule

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display=['stage', 'month', 'year']

class ExamModuleInline(admin.TabularInline):
    model=ExamModule
    extra=1

@admin.register(Exam)
class ExamenAdmin(admin.ModelAdmin):
    list_display=['user', 'career', 'stage', 'score']
    list_filter=['career','stage']
    inlines=[ExamModuleInline]


# Register your models here.
