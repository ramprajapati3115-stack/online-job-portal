# online-job-portal
# Job Portal - Django Project

A comprehensive job portal web application built with Django, allowing employers to post jobs and job seekers to apply for positions.

## 📋 Project Features

### For Job Seekers:
- User registration and authentication
- Browse and search job listings
- Filter jobs by location, job type, and experience level
- Apply for jobs with cover letter and resume
- Track application status
- View personal dashboard with application history

### For Employers:
- Company registration and profile management
- Post new job listings
- Edit existing job postings
- View and manage applications received
- Track applicant information and documents

### Admin Features:
- Manage all users, jobs, and applications
- Monitor platform activity
- User role management

## 🛠️ Technologies Used

- **Backend:** Python 3.x, Django 4.2
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap 5
- **Additional:** mysqlclient for MySQL connectivity

## 📦 Installation & Setup

### 1. Prerequisites
- Python 3.7 or higher installed
- MySQL Server installed and running
- pip package manager

### 2. Create MySQL Database
```bash
mysql -u root -p
```
```sql
CREATE DATABASE jobportal_db;
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Settings
Edit `jobportal/settings.py` and update the DATABASES section:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobportal_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Change this to your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 🗂️ Project Structure

```
jobportal/
├── jobportal/                   # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── __init__.py
├── jobs/                        # Main application
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── job_list.html
│   │   ├── job_detail.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── complete_profile.html
│   │   ├── employer_dashboard.html
│   │   ├── job_seeker_dashboard.html
│   │   ├── post_job.html
│   │   ├── edit_job.html
│   │   ├── apply_job.html
│   │   └── view_applications.html
│   ├── static/                 # Static files (CSS, JS)
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── forms.py               # Django forms
│   ├── urls.py                # App URL routing
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App configuration
│   └── __init__.py
├── manage.py                   # Django management script
└── requirements.txt            # Project dependencies
```

## 📊 Database Models

### UserProfile
- Extended user profile with role-based access
- Supports Job Seeker, Employer, and Admin roles
- Stores company information and location

### Job
- Job listings with detailed information
- Includes salary range, experience level, and job type
- Status tracking (active, closed, draft)

### Application
- Job applications with cover letter and resume
- Application status tracking
- Links applicants with job postings

## 🚀 Usage

### For Job Seekers:
1. Register as a "Job Seeker"
2. Complete your profile
3. Browse available jobs
4. Apply for positions with your resume and cover letter
5. Track applications from your dashboard

### For Employers:
1. Register as an "Employer"
2. Complete company profile
3. Post new job listings
4. Review and manage applications
5. Track applicant information

### For Admin:
1. Access admin panel at `/admin/`
2. Login with superuser credentials
3. Manage users, jobs, and applications

## 🔐 Security Notes

⚠️ **Important:** Before deploying to production:
- Change the `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS` with your domain
- Use environment variables for sensitive data
- Set up HTTPS

## 📝 Common Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

## 🐛 Troubleshooting

### MySQL Connection Error
- Ensure MySQL server is running
- Check username and password in settings.py
- Verify database name exists

### Module Not Found Errors
- Run `pip install -r requirements.txt` again
- Check Python version compatibility

### Port Already in Use
- Use `python manage.py runserver 8001` to run on a different port

## 📞 Support

For issues or questions, please refer to the Django documentation:
- Django Docs: https://docs.djangoproject.com/
- MySQL Documentation: https://dev.mysql.com/doc/

## 📄 License

This project is created for educational purposes.

## 🎯 Future Enhancements

- Email notifications for new applications
- Advanced job search with filters
- User ratings and reviews
- Job recommendations based on profile
- Mobile app integration
- Payment integration for premium features
- Real-time chat between employers and applicants
- Skill verification system

---

**Created:** May 2024
**Last Updated:** May 2024
