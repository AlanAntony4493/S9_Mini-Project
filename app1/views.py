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
    return redirect('index')

def index_admin(request):
    if request.user.is_superuser:
        return render(request, "index.html")
    else:
        return redirect('index')


def index(request):
    return render(request, "index.html")

# event

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import AnswerReport, Donation, Event, Report
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
    return render(request,"index.html")

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

from django.core.mail import send_mail
from django.conf import settings

def approve_user(request, user_id):
    if request.user.is_superuser:
        user_profile = get_object_or_404(Registration, user__id=user_id)
    
        user_profile.is_approved = True 
        user_profile.is_active = True  # Set the user as active
        user_profile.save()

        
        subject = 'Account Approval for SMYM Mukkoottuthara'
        # message = f'Dear{user_profile.user.first_name}, ,We are thrilled to inform you that your registration request for Adonai has been approved by our admin team, and your account is now ready for use.You can now access all the exciting features and content available on our platform by logging in with your registered email address and password.We are committed to providing you with a seamless and enjoyable experience on Adonai, and we look forward to having you as an active member of our community.If you have any questions, encounter any issues, or need assistance with anything related to our website, please do not hesitate to contact our support team at smymmukkoottuthara@gmail.com.Thank you for choosing Adonai. We hope you have a fantastic time exploring our platform.Best regards,President SMYM Mukkoottuthara Adonai{ user_profile.user.email }'
        message = f'Dear {user_profile.user.username},\n\n' \
          'We are thrilled to inform you that your registration request for Adonai has been approved by our admin team, and your account is now ready for use.\n\n' \
          'You can now access all the exciting features and content available on our platform by logging in with your registered email address and password.\n\n' \
          'To get started, please click the following link to log in:\n' \
          '"http://127.0.0.1:8000/login" : Log In to Adonai\n\n' \
          'We are committed to providing you with a seamless and enjoyable experience on Adonai, and we look forward to having you as an active member of our community.\n\n' \
          'If you have any questions, encounter any issues, or need assistance with anything related to our website, please do not hesitate to contact our support team at smymmukkoottuthara@gmail.com.\n\n' \
          'Thank you for choosing Adonai. We hope you have a fantastic time exploring our platform.\n\n' \
          'Best regards,\n' \
          'President \n'\
        'SMYM Mukkoottuthara \n'
        'Adonai'       
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [ user_profile.user.email ]

        send_mail(subject, message, from_email, recipient_list)
    
        return redirect('user_admin')
    else:
        # If the current user is not a superuser, redirect them to the login page
        return redirect('login')


from django.core.mail import send_mail
from django.conf import settings
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

         # Compose the email body
        subject =  'Account Suspension Notification'
        message = f'Dear {user_profile.user.first_name},\n' \
                  'We hope this message finds you well. We regret to inform you that your account on [Website Name] has been suspended temporarily due to the following reason:\n\n' \
                  'Suspension Reason: {{user_profile.comments}}\n' \
                  'Suspension Date: {{timezone.now()}}\n\n' \
                  'Your account will remain suspended until further notice. During this time, you will not be able to access your account or use the platform\'s features.\n\n' \
                  'If you believe this suspension is in error or have any questions regarding the suspension, please reach out to our support team at smymmukkoottuthara@gmail.com for assistance. We will do our best to address your concerns and provide clarification on the situation.\n\n' \
                  'We take account suspensions seriously and strive to maintain a safe and enjoyable environment for all users. We appreciate your understanding and cooperation in this matter.\n\n' \
                  'Thank you for your attention to this notification, and we hope to resolve this issue promptly.\n\n' \
                  'Best regards,\n' \
                  'President\n' \
                  'SMYM Mukkoottuthara\n' \
                  'smymmukkoottuthara@gmail.com'
        
        # Send the email
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user_profile.user.email]
         
        send_mail(subject, message, from_email, recipient_list)

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



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Registration  # Import your Registration model

@login_required
def profile(request):
    user = request.user
    registration = Registration.objects.get(user=user)  # Retrieve Registration data

    context = {
        'user': user,
        'registration': registration,
    }
    return render(request, 'profile.html', context)



# career 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def career_forum(request):
    return render(request, 'career_forum.html')

# from django.shortcuts import render, redirect
# from .models import Question, Answer
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse

# @login_required
# def post_question(request):
#     if request.method == 'POST':
#         title = request.POST.get('questionTitle')
#         description = request.POST.get('questionDescription')
#         additional_details = request.POST.get('additionalDetails')
#         user = request.user

#         question = Question.objects.create(
#             title=title,
#             description=description,
#             additional_details=additional_details,
#             posted_by=user
#         )
#         question.save()
#         return redirect('career_forum')  # Redirect to the career forum page

# @login_required
# def post_answer(request):
#     if request.method == 'POST':
#         answer_text = request.POST.get('answerText')
#         question_id = request.POST.get('questionId')
#         user = request.user

#         question = Question.objects.get(pk=question_id)

#         answer = Answer.objects.create(
#             question=question,
#             text=answer_text,
#             posted_by=user
#         )
#         answer.save()
#         return JsonResponse({'success': True})

# def get_questions_and_answers(request):
#     # Fetch and prepare the list of questions and answers from your database
#     questions = Question.objects.all()
#     answers = Answer.objects.all()
    
#     data = {
#         'questions': [{'title': q.title, 'description': q.description, 'id': q.id} for q in questions],
#         'answers': [{'text': a.text, 'user': a.posted_by.username, 'question_id': a.question.id} for a in answers],
#     }
    
#     return JsonResponse(data)


# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

@login_required
def post_question(request):
    if request.method == 'POST':
        title = request.POST.get('questionTitle')
        description = request.POST.get('questionDescription')
        additional_details = request.POST.get('additionalDetails')
        user = request.user

        question = Question.objects.create(
            title=title,
            description=description,
            additional_details=additional_details,
            posted_by=user
        )

        # Optionally, you can redirect to the career_forum page after posting
        return redirect('career_forum')
    else:
        return JsonResponse({'success': False})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

@login_required
def post_answer(request):
    if request.method == 'POST':
        # print(answer_text)
        answer_text = request.POST.get('answerText')
        question_id = request.POST.get('questionId')
        user = request.user
        # print('answer_text')
        question = Question.objects.get(pk=question_id)

        answer = Answer.objects.create(
            question=question,
            answer_text=answer_text,
            posted_by=user
        )

        # Optionally, you can redirect to the career_forum page after posting
        return redirect('career_forum')
    else:
        return JsonResponse({'success': False})


from django.shortcuts import render
from .models import Question, Answer

def career_forum(request):
    # Fetch and prepare the list of questions and answers from your database
    # questions = Question.objects.all()
    # answers = Answer.objects.filter(is_deleted=False)
    questions = Question.objects.select_related('posted_by__registration').all()
    answers = Answer.objects.filter(is_deleted=False).select_related('posted_by__registration')

    context = {
        'questions': questions,
        'answers': answers,
    }
    
    return render(request, 'career_forum.html', context)


from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Question, Answer

@login_required
def soft_delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        question.is_deleted = True
        question.save()
        return redirect('career_forum')  # Redirect to the career forum page after soft delete
    else:
        return JsonResponse({'success': False})

from django.http import JsonResponse

def soft_delete_answer(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
        answer.is_deleted = True
        answer.save()
        return redirect('career_forum')
    except Answer.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Answer not found'})


from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))




# views.py
from django.http import JsonResponse

def edit_comment(request, answer_id):
    if request.method == 'POST':
        edited_text = request.POST.get('edited_text')

        try:
            # Find the comment by its ID and update the text
            comment = Answer.objects.get(pk=answer_id)
            comment.answer_text = edited_text
            comment.save()

            return JsonResponse({'success': True})
        except Answer.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Comment not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})



from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def report_comment(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    reason = request.POST.get('reason', '')

    if reason:
        # Create an AnswerReport object and save it to the database
        report = AnswerReport(answer=answer, reporter=request.user, reason=reason)
        report.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


from django.shortcuts import render
from django.db.models import Count, Subquery, OuterRef
from .models import AnswerReport, Answer

def reported_comments(request):
    # Subquery to count reports for each answer
    report_counts = AnswerReport.objects.filter(answer=OuterRef('pk')).values('answer').annotate(report_count=Count('id')).values('report_count')

    # Query the reported answers with counts
    reported_answers = Answer.objects.filter(
        answerreport__in=Subquery(report_counts)
    ).annotate(report_count=Subquery(report_counts)).distinct()

    return render(request, 'reported_comments.html', {'reported_answers': reported_answers})




from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def donation_form(request):
	currency = 'INR'
	amount = 20000 # Rs. 200

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['callback_url'] = callback_url

	return render(request, 'donation_form.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 20000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)

					# render success page on successful caputre of payment
					return render(request, 'paymentsuccess.html')
				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()
