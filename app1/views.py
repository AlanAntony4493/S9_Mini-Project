from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        Mname = request.POST['Mname']
        Hname = request.POST['Hname']
        prayerGroup = request.POST['prayerGroup']
        dob = request.POST['dob']
        gender = request.POST['gender']
        mob = request.POST['mob']

        # Check if a user with the same email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name, password=password)

        registration = Registration(
            user=user,
            middle_name=Mname,
            house_name=Hname,
            prayer_group=prayerGroup,
            date_of_birth=dob,
            gender=gender,
            phone_number=mob,
        )
        registration.fname = first_name
        registration.lname = last_name
        registration.save()
        return redirect('login')
    return render(request, 'register.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('index_admin')
            elif user.registration.is_approved:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'User is not approved yet. Please wait for approval.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'login.html')



from django.contrib.auth.models import User, auth
def logout(request):
    auth.logout(request)
    return redirect("index")


def index_admin(request):
    if request.user.is_superuser:
        return render(request, "index_admin.html")
    else:
        return redirect('index')


def index(request):
    return render(request, "index.html")

# event

from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.utils import timezone

def event(request):
    tomorrow = timezone.now() + timezone.timedelta(days=1)
    context = {'tomorrow': tomorrow}

    if request.method == 'POST':
        # Retrieve data from the request and create an Event object
        date = request.POST['date']
        title = request.POST['title']
        description = request.POST['description']
        start_time = request.POST['start-time']
        end_time = request.POST['end-time']
        venue = request.POST['venue']
        cover_poster = request.FILES.get('cover-poster')
        detailed_poster = request.FILES.get('detailed-poster')

        event = Event(
            date=date,
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            venue=venue,
            cover_poster=cover_poster,
            detailed_poster=detailed_poster
        )
        event.save()

        # Redirect to a success page or event list (replace 'event' with your actual URL pattern)
        return redirect('event')

    # Fetch existing events, including archived ones
    events = Event.objects.all()

    # Separate archived and non-archived events
    non_archived_events = events.filter(is_archived=False)
    archived_events = events.filter(is_archived=True)

    context['events'] = non_archived_events
    context['archived_events'] = archived_events

    return render(request, 'event.html', context)

def archive_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.is_archived = True
    event.save()
    return redirect('event')

def unarchive_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.is_archived = False
    event.save()
    return redirect('event') 

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('event')



def by_law(request):
    return render(request,"by_law.html")

def index_home(request):
    return render(request,"index_home.html")

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Donor

def blood_admin(request):
    donors = Donor.objects.all()
    is_superuser = request.user.is_superuser if request.user.is_authenticated else False

    if request.method == 'POST' and is_superuser:
        name = request.POST.get('funame')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood-group')
        contact = request.POST.get('mob')

        donor = Donor(
            name=name,
            age=age,
            gender=gender,
            blood_group=blood_group,
            contact=contact
        )
        donor.save()

        # messages.success(request, 'Donor data submitted successfully.')
        return redirect('blood_admin')  

    return render(request, 'blood_admin.html', {'donors': donors, 'is_superuser': is_superuser})

    

def approve_user(request, user_id):
   
    if request.user.is_superuser:
       
        user_profile = get_object_or_404(Registration, user__id=user_id)

    
        user_profile.is_approved = True 
        user_profile.save()

        # Redirect back to the user administration page
        return redirect('user_admin')
    else:
        # If the current user is not a superuser, redirect them to the login page
        return redirect('login')


def delete_user(request, user_id):
    user_profile = get_object_or_404(Registration, user__id=user_id)
    user_profile.user.delete()
    return redirect('user_admin')  


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Registration  

@login_required
def user_admin(request):
    if request.user.is_superuser:
        users = User.objects.all()
        user_profiles = Registration.objects.select_related('user').all()
        context = {
            'users': users,
            'user_profiles': user_profiles,
        }
        return render(request, 'user_admin.html', context)
    else:
        return redirect('login')

def filtered_donor_list(request, blood_group):
    donors = Donor.objects.filter(blood_group=blood_group)
    return render(request, 'blood_user.html', {'donors': donors})

def delete_donor(request,pk):
    donors= get_object_or_404(Donor, id=pk)
    donors.delete()
    return redirect('blood_admin')

# parish directory

from django.shortcuts import render, redirect
from .models import PrayerGroup, ParishDirectory
from django.db import IntegrityError

def parish_admin(request):
    error_message = None  # Initialize error message to None
    if request.method == 'POST':
       # Check which form was submitted based on the presence of specific POST data
        if 'new_group_name' in request.POST:
            # Process the POST data to add a new prayer group
            new_group_name = request.POST.get('new_group_name')
            if new_group_name:
                try:
                    PrayerGroup.objects.create(name=new_group_name)
                except IntegrityError:
                    error_message = "A prayer group with this name already exists."
        else:
            # Process the POST data to add a new member to the parish directory
            name = request.POST.get('funame')
            house_name = request.POST.get('Hname')
            contact = request.POST.get('mob')
            prayer_group_id = request.POST.get('prayer_group')
            if name and house_name and contact and prayer_group_id:
                prayer_group = PrayerGroup.objects.get(pk=prayer_group_id)
                ParishDirectory.objects.create(
                    name=name,
                    house_name=house_name,
                    contact=contact,
                    prayer_group=prayer_group
                )
        return redirect('parish_admin')  # Redirect to the parish admin page

    # Fetch the list of prayer groups
    prayer_groups = PrayerGroup.objects.all()

    # Fetch the list of parish members along with their associated prayer groups
    parish_members = ParishDirectory.objects.select_related('prayer_group').all()

    return render(request, 'parish_admin.html', {'prayer_groups': prayer_groups, 'parish_members': parish_members, 'error_message': error_message})

# report

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report

def report_admin(request):
    if request.method == 'POST':
        if request.user.is_staff:  # Check if the user is a staff member (admin)
            heading = request.POST.get('heading')
            report_text = request.POST.get('report')
            date = request.POST.get('date')
            place = request.POST.get('place')
            funame = request.POST.get('funame')

            Report.objects.create(
                heading=heading,
                report=report_text,
                date=date,
                place=place,
                name=funame
            )

            # messages.success(request, 'Report successfully added.')
            return redirect('report_admin')  # Redirect after successful submission
        else:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('login')  # Redirect to the login page for non-admin users

    # Fetch the latest report entry from the database based on the latest date
    latest_report = Report.objects.latest('date')

    # Fetch all reports for the dropdown
    reports = Report.objects.all().order_by('-date')

    return render(request, 'report_admin.html', {'latest_report': latest_report, 'reports': reports})


def gallery(request):
    return render(request, 'gallery.html')

# career 
def career_forum(request):
    return render(request, 'career_forum.html')
