from django.contrib import admin
from .models import UserProfile, Job, Application


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'company_name', 'location']
    list_filter = ['role', 'created_at']
    search_fields = ['user__username', 'company_name']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'job_type', 'experience_level', 'status', 'posted_date']
    list_filter = ['status', 'job_type', 'experience_level', 'posted_date']
    search_fields = ['title', 'description', 'company__company_name']
    readonly_fields = ['posted_date', 'updated_date']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_date']
    list_filter = ['status', 'applied_date']
    search_fields = ['applicant__user__username', 'job__title']
    readonly_fields = ['applied_date', 'updated_date']
