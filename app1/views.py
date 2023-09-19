from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.urls import reverse

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


from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('index')
            elif user.registration.is_active and user.registration.is_approved:
                login(request, user)
                return redirect('index')
            elif not user.registration.is_active:
                messages.error(request, 'User account is not active.')
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

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Event, Report
from django.utils import timezone

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg', 'ico', 'jfif', 'pjpeg', 'pjp', 'avif']

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

        # Validate file extensions
        cover_extension = cover_poster.name.split('.')[-1].lower() if cover_poster else None
        detailed_extension = detailed_poster.name.split('.')[-1].lower() if detailed_poster else None

        if (cover_extension not in ALLOWED_EXTENSIONS) or (detailed_extension not in ALLOWED_EXTENSIONS):
            # Create a custom error message
            error_message = 'File must be an image with a valid extension (jpg, jpeg, png, gif, bmp, tiff, webp, svg, ico, jfif, pjpeg, pjp, avif).'
            context['error_message'] = error_message
        else:
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

from django.utils import timezone

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

def del_event(request, event_id):
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
    donors = Donor.objects.filter(is_deleted=False)
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

from django.shortcuts import get_object_or_404, redirect, reverse  # Import the reverse function
from .models import Donor

def soft_delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    donor.is_deleted = True
    donor.save()

    # Use reverse to get the URL for the blood_admin page
    return redirect(reverse('blood_admin'))

def approve_user(request, user_id):
    if request.user.is_superuser:
        user_profile = get_object_or_404(Registration, user__id=user_id)
    
        user_profile.is_approved = True 
        user_profile.is_active = True  # Set the user as active
        user_profile.save()
    
        return redirect('user_admin')
    else:
        # If the current user is not a superuser, redirect them to the login page
        return redirect('login')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Registration

def delete_user(request, user_id):
    user_profile = get_object_or_404(Registration, user__id=user_id)
    
    if request.method == 'POST':
        comment = request.POST.get('comments', '')
        user_profile.is_active = False
        user_profile.comments = comment
        user_profile.save()
        
        # You can add any additional logic or messages here if needed
        
        return redirect('user_admin')
    
    return render(request, 'user_admin.html', {'user_profile': user_profile})
  


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Registration

@login_required
def user_admin(request):
    if request.user.is_superuser:
        # Get all user profiles
        user_profiles = Registration.objects.select_related('user').all()

        # Separate profiles into three lists based on approval status
        pending_approval_users = [profile for profile in user_profiles if not profile.is_approved and profile.is_active]
        approved_users = [profile for profile in user_profiles if profile.is_approved and profile.is_active]
        rejected_users = [profile for profile in user_profiles if not profile.is_active]

        context = {
            'pending_approval_users': pending_approval_users,
            'approved_users': approved_users,
            'rejected_users': rejected_users,
        }
        return render(request, 'user_admin.html', context)
    else:
        return redirect('login')


def filtered_donor_list(request, blood_group):
    donors = Donor.objects.filter(blood_group=blood_group)
    return render(request, 'blood_user.html', {'donors': donors})

# def delete_donor(request,pk):
#     donors= get_object_or_404(Donor, id=pk)
#     donors.delete()
#     return redirect('blood_admin')

# views.py

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import PrayerGroup, ParishDirectory
from django.db.models import Q

def parish_admin(request):
    error_message = None

    if request.method == 'POST':
        if 'new_group_name' in request.POST:
            new_group_name = request.POST.get('new_group_name')
            if new_group_name:
                # Check if the group name already exists (case-insensitive)
                if PrayerGroup.objects.filter(Q(name__iexact=new_group_name) & ~Q(is_deleted=True)).exists():
                    error_message = "A prayer group with this name already exists."
                else:
                    try:
                        PrayerGroup.objects.create(name=new_group_name)
                    except IntegrityError:
                        error_message = "An error occurred while creating the prayer group."
        else:
            form_name = request.POST.get('funame')
            form_house_name = request.POST.get('Hname')
            form_contact = request.POST.get('mob')
            prayer_group_id = request.POST.get('prayer_group')

            if form_name and form_house_name and form_contact and prayer_group_id:
                prayer_group = PrayerGroup.objects.get(pk=prayer_group_id)
                ParishDirectory.objects.create(
                    name=form_name,
                    house_name=form_house_name,
                    contact=form_contact,
                    prayer_group=prayer_group
                )

    elif request.method == 'GET':
        error_message = None  # Initialize the error message
        if 'soft_delete_group' in request.GET:
            group_id = request.GET.get('soft_delete_group')
            try:
                group = PrayerGroup.objects.get(pk=group_id)
                group.is_deleted = True
                group.save()

                # Soft delete all related Parish Members
                ParishDirectory.objects.filter(prayer_group=group).update(is_deleted=True)

            except PrayerGroup.DoesNotExist:
                error_message = "The selected prayer group does not exist."

            # Redirect back to the parish_admin page after group deletion
            return HttpResponseRedirect(reverse('parish_admin'))

        elif 'soft_delete_member' in request.GET:
            member_id = request.GET.get('soft_delete_member')
            try:
                member = ParishDirectory.objects.get(pk=member_id)
                member.is_deleted = True
                member.save()

            except ParishDirectory.DoesNotExist:
                error_message = "The selected parish member does not exist."

            # Redirect back to the parish_admin page after member deletion
            return HttpResponseRedirect(reverse('parish_admin'))

    prayer_groups = PrayerGroup.objects.filter(is_deleted=False)
    parish_members = ParishDirectory.objects.select_related('prayer_group').filter(is_deleted=False)
    deleted_prayer_groups = PrayerGroup.objects.filter(is_deleted=True)
    deleted_parish_members = ParishDirectory.objects.filter(is_deleted=True)

    return render(request, 'parish_admin.html', {
        'prayer_groups': prayer_groups,
        'parish_members': parish_members,
        'deleted_prayer_groups': deleted_prayer_groups,
        'deleted_parish_members': deleted_parish_members,
        'error_message': error_message,
    })


from django.shortcuts import redirect
from django.contrib import messages

def retrieve_deleted_entity(request, entity_type, entity_id):
    retrieve_error_message = None  # Initialize the error message

    try:
        if entity_type == 'prayer_group':
            group = PrayerGroup.objects.get(pk=entity_id)
            group.is_deleted = False
            group.save()

            # Set the is_deleted flag to False for related Parish Members
            ParishDirectory.objects.filter(prayer_group=group).update(is_deleted=False)

        elif entity_type == 'parish_member':
            member = ParishDirectory.objects.get(pk=entity_id)

            # Check if the related prayer group is deleted
            if member.prayer_group.is_deleted:
                retrieve_error_message = "The chosen participant's prayer group is not active or dosen't exist"
            else:
                member.is_deleted = False
                member.save()
        else:
            raise ValueError("Invalid entity type.")

    except (PrayerGroup.DoesNotExist, ParishDirectory.DoesNotExist, ValueError) as e:
        retrieve_error_message = str(e)  # Convert the exception to a string

    # Store the error message in the Django messages framework
    if retrieve_error_message:
        messages.error(request, retrieve_error_message)

    # Redirect back to the 'parish_admin' page
    return redirect('parish_admin')


def gallery(request):
    return render(request, 'gallery.html')

# career 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def career_forum(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        Question.objects.create(user=request.user, question_text=question_text)
        messages.success(request, 'Question posted successfully.')
        return redirect('career_forum')

    questions = Question.objects.all().order_by('-created_at')
    for question in questions:
        question.answers = question.answers.all().order_by('-created_at')

    return render(request, 'career_forum.html', {'questions': questions})

@login_required
def view_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answers.all()

    if request.method == 'POST':
        answer_text = request.POST.get('answer_text')
        Answer.objects.create(user=request.user, question=question, answer_text=answer_text)
        messages.success(request, 'Answer posted successfully.')
        return redirect('view_question', question_id=question.id)

    return render(request, 'view_question.html', {'question': question, 'answers': answers})

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user == question.user:
        question.delete()
        messages.success(request, 'Question deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this question.')

    return redirect('career_forum')

@login_required
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user == answer.user:
        answer.delete()
        messages.success(request, 'Answer deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this answer.')

    return redirect('view_question', question_id=answer.question.id)


from django.db import IntegrityError
def report_admin(request):
    # Fetch all reports for the dropdown
    reports = Report.objects.all().order_by('-date')

    try:
        # Fetch the latest report entry from the database based on the latest date
        latest_report = Report.objects.latest('date')
    except Report.DoesNotExist:
        # Handle the case when no reports exist
        latest_report = None

    if request.method == 'POST':
        if request.user.is_staff:  # Check if the user is a staff member (admin)
            heading = request.POST.get('heading')
            report_text = request.POST.get('report')
            date = request.POST.get('date')
            place = request.POST.get('place')
            funame = request.POST.get('funame')

            try:
                Report.objects.create(
                    heading=heading,
                    report=report_text,
                    date=date,
                    place=place,
                    name=funame
                )
            except IntegrityError:
                messages.error(request, 'A report with the same date already exists.')
            
            return redirect('report_admin')  # Redirect after submission

        else:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('login')  # Redirect to the login page for non-admin users

    return render(request, 'report_admin.html', {'latest_report': latest_report, 'reports': reports})





# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import ParishDirectory

def update_parish(request, member_id):
    parish_member = get_object_or_404(ParishDirectory, id=member_id)
    prayer_groups = PrayerGroup.objects.filter(is_deleted=False)

    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        house_name = request.POST.get('house_name')
        contact = request.POST.get('contact')
        prayer_group_id = request.POST.get('prayer_group')

        # Update the Parish Directory record
        prayer_group = PrayerGroup.objects.get(pk=prayer_group_id)
        
        parish_member.name = name
        parish_member.house_name = house_name
        parish_member.contact = contact
        parish_member.prayer_group = prayer_group
        parish_member.save()

        return redirect('parish_admin')  # Redirect to the parish_admin page after update

    return render(request, 'update_parish.html', {'parish_member': parish_member, 'prayer_groups': prayer_groups})




