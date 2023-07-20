from django.shortcuts import render,redirect
from .models import Project,Skill,Message,Endorsement,Comment
from .forms import ProjectForm,MessageForm,SkillForm,EndorsementForm,CommentForm,OrderForm,QuestionForm
from django.conf import settings
from django.contrib import messages
from django import http
from django.urls import reverse
import razorpay
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponseBadRequest

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import user_passes_test,login_required


# Create your views here.
def home(request):
    projects  = Project.objects.all()
    skills = Skill.objects.exclude(body='')
    other_skills = Skill.objects.filter(body='')

    endorsements = Endorsement.objects.filter(approved=True)

    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
            messages.success(request,'Your message was sent successfully...')

    context = {
        "projects" : projects,
        "skills" : skills,
        "other_skills" : other_skills,
        "form" : form,
        "endorsements" : endorsements,
        "navbar" : "home",
    }
    return render(request,'core/home.html',context)

def aboutPage(request):
    context = {
        "navbar" : "about",
    }
    return render(request,'core/about.html',context)

def contactPage(request):
    context = {
        "navbar" : "contact",
    }
    return render(request,'core/contact.html',context)

@csrf_exempt
def projectPage(request,pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count
    comments = project.comment_set.all().order_by('-created')

    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request,'Your comment was added successfully...')
            return http.HttpResponseRedirect(reverse('project',args=[pk]))

    context = {
        "project" : project,
        "count" : count,
        "comments" : comments,
        "form" : form,
        "navbar" : "project",
    }
    return render(request,'core/project.html',context)

@csrf_exempt
def addProject(request):

    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {
        "form" : form,
        "navbar" : "add-project"
    }
    return render(request,'core/project_form.html',context)

@csrf_exempt
def editProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {
        "form" : form,
    }
    return render(request,'core/project_form.html',context)

@csrf_exempt
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("home")
    
    context = {
        "project" : project,
    }
    return render(request,'core/delete_project.html',context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unread_cnt = Message.objects.filter(is_read=False).count()
    context = {
        "inbox" : inbox,
        "unread_cnt" : unread_cnt,
        "navbar" : "inbox"
    }
    return render(request,'core/inbox.html',context)

def messagePage(request,pk):
    message = Message.objects.get(id=pk)
    message.is_read=True
    message.save()
    context = {
        "message" : message,
    }
    return render(request,'core/message.html',context)

@csrf_exempt
def addSkill(request):
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)
        form.save()
        messages.success(request,'Your skill was added successfully...')
        return redirect('home')
    
    context = {
        "form" : form,
        "navbar" : "add-skill",
    }
    return render(request,'core/skill_form.html',context)

@csrf_exempt
@login_required
def addEndorsement(request):
    form = EndorsementForm()

    if request.method == "POST":
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request,'Thank You, Your endorsement was added successfully...')
        return redirect('home')
    
    context = {
        "form" : form,
    }
    return render(request,'core/endorsement_form.html',context)

@csrf_exempt
def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100

        # create Razorpay client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        # create order
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            order = Coffee(
                name=name,
                amount=amount,
                order_id=order_id,
            )
            order.save()
            response_payment['name'] = name

            form = OrderForm(request.POST or None)
            return render(request, 'core/payment.html', {'form': form, 'payment': response_payment})

    form = OrderForm()
    return render(request, 'core/payment.html', {'form': form, 'navbar' : 'donation'})

@csrf_exempt
def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        order = Coffee.objects.get(order_id=response['razorpay_order_id'])
        order.razorpay_payment_id = response['razorpay_payment_id']
        order.paid = True
        order.save()
        return render(request, 'core/callback.html', {'status': True})
    except:
        return render(request, 'core/callback.html', {'status': False})

@csrf_exempt
def chartPage(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        form.save()
        messages.success(request,'Thanks for your vote!')
        return redirect('chart')
    
    context = {
        'form' : form,
        'navbar' : 'vote',
    }
    return render(request,'core/chart.html',context)

@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('pass')
        user  = authenticate(request,username=uname,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"User was logged in successfully...")
            return redirect('home')
        else:
            messages.error(request,"Username or Password is incorrect!!!")


    context = {
        'navbar' : 'login',
    }
    return render(request,"core/login_page.html",context)

@csrf_exempt
def signupPage(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request,'Both password field should be matched....')
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            messages.success(request,"Your account was created successfully!!")
            return redirect('login')


    context = {
        'navbar' : 'login',
    }
    return render(request,'core/register_page.html',context)

@csrf_exempt
def logoutPage(request):

    if request.method == 'POST':
        logout(request)
        return redirect("home")
    
    context = {
        'navbar' : 'logout',
    }
    return render(request,"core/logout.html",context)


