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
                return redirect('index_home')
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

# event admin
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Event

from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Event  # Import your Event model

def event(request):
    tomorrow = datetime.now() + timedelta(days=1)
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

        # Redirect to a success page or event list (replace 'event-list' with your actual URL pattern)
        return redirect('event')  

    # Fetch existing events for display
    events = Event.objects.all()
    context['events'] = events

    return render(request, 'event.html', context)


def by_law(request):
    return render(request,"by_law.html")

def index_home(request):
    return render(request,"index_home.html")

from .models import Donor  # Import the Donor model
def blood_admin(request):
    donors = Donor.objects.all()
    if request.method == 'POST':
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
 
    return render(request, 'blood_admin.html', {'donors': donors})
    

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

def event_user(request):
    events = Event.objects.all()
    return render(request, 'event_user.html',{'events': events})

def blood_user(request):
    donors = Donor.objects.all()
    return render(request, 'blood_user.html', {'donors': donors})

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

def parish_admin(request):
    if request.method == 'POST':
        # Check which form was submitted based on the presence of specific POST data
        if 'new_group_name' in request.POST:
            # Process the POST data to add a new prayer group
            new_group_name = request.POST.get('new_group_name')
            if new_group_name:
                PrayerGroup.objects.create(name=new_group_name)
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

    return render(request, 'parish_admin.html', {'prayer_groups': prayer_groups, 'parish_members': parish_members})

# parish directory user

def parish_user(request):
    parish_members = ParishDirectory.objects.all()
    return render(request, 'parish_user.html', {'parish_members': parish_members})


# report
def report_admin(request):
    return render(request, "report_admin.html")