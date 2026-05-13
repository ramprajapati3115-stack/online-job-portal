from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Job, Application, UserProfile
from .forms import UserRegistrationForm, UserProfileForm, JobForm, ApplicationForm, JobSearchForm
from django.contrib.auth.models import User


# Home Page
def home(request):
    recent_jobs = Job.objects.filter(status='active').order_by('-posted_date')[:6]
    total_jobs = Job.objects.filter(status='active').count()
    context = {
        'recent_jobs': recent_jobs,
        'total_jobs': total_jobs,
    }
    return render(request, 'home.html', context)


# Job Listing Page
def job_list(request):
    jobs = Job.objects.filter(status='active')
    form = JobSearchForm(request.GET or None)
    
    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        location = form.cleaned_data.get('location')
        job_types = form.cleaned_data.get('job_type')
        experience_levels = form.cleaned_data.get('experience_level')
        
        if keyword:
            jobs = jobs.filter(
                Q(title__icontains=keyword) |
                Q(description__icontains=keyword)
            )
        
        if location:
            jobs = jobs.filter(location__icontains=location)
        
        if job_types:
            jobs = jobs.filter(job_type__in=job_types)
        
        if experience_levels:
            jobs = jobs.filter(experience_level__in=experience_levels)
    
    context = {
        'jobs': jobs,
        'form': form,
    }
    return render(request, 'job_list.html', context)


# Job Detail Page
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    applications = Application.objects.filter(job=job)
    user_has_applied = False
    
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_has_applied = Application.objects.filter(
                job=job,
                applicant=user_profile
            ).exists()
        except UserProfile.DoesNotExist:
            pass
    
    context = {
        'job': job,
        'applications': applications,
        'user_has_applied': user_has_applied,
    }
    return render(request, 'job_detail.html', context)


# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        profile_form = UserProfileForm()
    
    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'register.html', context)


# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('job_list')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


# User Logout
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


# User Dashboard
@login_required(login_url='login')
def user_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('complete_profile')
    
    if user_profile.role == 'employer':
        jobs = Job.objects.filter(company=user_profile)
        context = {
            'user_profile': user_profile,
            'jobs': jobs,
        }
        return render(request, 'employer_dashboard.html', context)
    else:
        applications = Application.objects.filter(applicant=user_profile)
        context = {
            'user_profile': user_profile,
            'applications': applications,
        }
        return render(request, 'job_seeker_dashboard.html', context)


# Complete Profile
@login_required(login_url='login')
def complete_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_dashboard')
    else:
        form = UserProfileForm(instance=user_profile)
    
    context = {
        'form': form,
    }
    return render(request, 'complete_profile.html', context)


# Post Job (Employer only)
@login_required(login_url='login')
def post_job(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user, role='employer')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Only employers can post jobs.')
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = user_profile
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('user_dashboard')
    else:
        form = JobForm()
    
    context = {
        'form': form,
    }
    return render(request, 'post_job.html', context)


# Edit Job
@login_required(login_url='login')
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if job.company != user_profile:
            messages.error(request, 'You do not have permission to edit this job.')
            return redirect('user_dashboard')
    except UserProfile.DoesNotExist:
        return redirect('complete_profile')
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('user_dashboard')
    else:
        form = JobForm(instance=job)
    
    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'edit_job.html', context)


# Apply for Job
@login_required(login_url='login')
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    try:
        user_profile = UserProfile.objects.get(user=request.user, role='job_seeker')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Only job seekers can apply for jobs.')
        return redirect('job_detail', job_id=job.id)
    
    try:
        existing_application = Application.objects.get(job=job, applicant=user_profile)
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', job_id=job.id)
    except Application.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = user_profile
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_seeker_dashboard')
    else:
        form = ApplicationForm()
    
    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'apply_job.html', context)


# View Applications (Employer only)
@login_required(login_url='login')
def view_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if job.company != user_profile:
            messages.error(request, 'You do not have permission to view these applications.')
            return redirect('user_dashboard')
    except UserProfile.DoesNotExist:
        return redirect('complete_profile')
    
    applications = Application.objects.filter(job=job)
    
    context = {
        'job': job,
        'applications': applications,
    }
    return render(request, 'view_applications.html', context)
