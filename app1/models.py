from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=50, blank=True)
    house_name = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # New field for user status
    comments = models.TextField(blank=True) 
    
    PRAYER_GROUP_CHOICES = [
        ('Gethsemane', 'Gethsemane'),
        ('Emmaus', 'Emmaus'),
        ('Jerusalem', 'Jerusalem'),
        ('Badhaniya', 'Badhaniya'),
        ('Jericho', 'Jericho'),
        ('Parudeesa', 'Parudeesa'),
        ('Samaria', 'Samaria'),
        ('Bethlehem', 'Bethlehem'),
        ('Galilee', 'Galilee'),
        ('Capernaum', 'Capernaum'),
        ('Kana', 'Kana'),
        ('Jordan', 'Jordan'),
        ('Calvary', 'Calvary'),
    ]
    prayer_group = models.CharField(max_length=20, choices=PRAYER_GROUP_CHOICES)
    date_of_birth = models.DateField()
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s Registration"


class Donor(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUP_CHOICES)
    
    contact = models.CharField(max_length=20)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name



# parish directory

# prayer group 
class PrayerGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_deleted = models.BooleanField(default=False)  # Add this field

    def __str__(self):
        return self.name

# Model for Parish Directory
class ParishDirectory(models.Model):
    name = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, unique=True)
    prayer_group = models.ForeignKey(PrayerGroup, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

# event

class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=100)
    cover_poster = models.ImageField(upload_to='event_covers', default='img/about.jpg')
    detailed_poster = models.ImageField(upload_to='detailed_posters')
    is_archived = models.BooleanField(default=False)

# report

class Report(models.Model):
    heading = models.CharField(max_length=500)
    report = models.TextField()
    date = models.DateField(unique=True)
    place = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    additional_details = models.TextField(blank=True, null=True)
    posted_date_time = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    posted_date_time = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)  # Soft delete flag

    def __str__(self):
        return self.answer_text


# models.py

from django.db import models
from django.contrib.auth.models import User

class AnswerReport(models.Model):
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f"Reported by {self.reporter.username}"



# models.py

from django.db import models

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Donation of {self.amount} on {self.timestamp}"




# gallery

from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='albums/covers/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models
from .models import Album

class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='albums/images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description



class CareerResourcePerson(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # You can adjust the max_length as needed
    photo = models.ImageField(upload_to='resource_person_photos/', blank=False)  # No longer allows null values

    def __str__(self):
        return self.name
