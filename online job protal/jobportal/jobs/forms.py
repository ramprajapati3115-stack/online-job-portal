from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Job, Application


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='Password'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        label='Confirm Password'
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Passwords do not match!")
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'phone_number', 'company_name', 'bio', 'location']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Bio'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'location', 'salary_min', 'salary_max', 
                  'job_type', 'experience_level', 'status', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job Description'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Requirements'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Salary'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Maximum Salary'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'experience_level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Cover Letter'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
        }


class JobSearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search jobs by keyword...'}),
        label='Keyword'
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        label='Location'
    )
    job_type = forms.MultipleChoiceField(
        required=False,
        choices=[
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('contract', 'Contract'),
            ('internship', 'Internship'),
        ],
        widget=forms.CheckboxSelectMultiple(),
        label='Job Type'
    )
    experience_level = forms.MultipleChoiceField(
        required=False,
        choices=[
            ('entry', 'Entry Level'),
            ('mid', 'Mid Level'),
            ('senior', 'Senior Level'),
        ],
        widget=forms.CheckboxSelectMultiple(),
        label='Experience Level'
    )
