from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=50, blank=True)
    house_name = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False)
    
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

    def __str__(self):
        return self.name



# parish directory

# Model for Prayer Groups
class PrayerGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Parish Directory
class ParishDirectory(models.Model):
    name = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, unique=True)  # Add unique=True here
    prayer_group = models.ForeignKey(PrayerGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# event

class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    end_date = models.DateField()
    venue = models.CharField(max_length=100)
    cover_poster = models.ImageField(upload_to='event_covers', default='img/about.jpg')
    detailed_poster = models.ImageField(upload_to='detailed_posters')