from django.shortcuts import render, get_object_or_404 , HttpResponse
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, dieticians, appointments
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib.auth.models import User
import nltk , re
nltk.download('punkt')
from nltk.tokenize import word_tokenize
stop_words =['hell', 'cheat','http','stupid','nonsense','fraud','bad','palgarism','negative','shit',
             'shut up','mouth','keep shut','abuse','abusive','kill','get lost','bustard']

def home(request):
    user_context={
        'users': Post.objects.all()
    }
    #return HttpResponse(request, user_context['users'])
    return render(request, 'blog\home.html')

def blog_part(request):
    post_context = {
        'post_list': Post.objects.order_by('-date_posted')
    }
    connect_context ={
        'diet_list': dieticians.objects.order_by('tot_rank_score')[::-1]
    }
    if request.method == "POST":
        if request.POST.get('getbookmark'):
            get_id = request.POST.get('getbookmark')
            post_row = get_object_or_404(Post, pk=get_id)
            post_row.bookmark = "MARK"
            post_row.save()
            messages.success(request, 'Bookmark Saved! View it on bookmarks tab.')
            return render(request, 'blog\\blog.html', post_context)
        if request.POST.get('getcbookmark'):
            get_id = request.POST.get('getcbookmark')
            diet_row = get_object_or_404(dieticians, pk=get_id)
            diet_row.bookmark = "MARK"
            diet_row.save()
            messages.success(request, 'Bookmark Saved! View it on bookmarks tab.')
            return render(request, 'blog\connect.html', connect_context)
    else:
        #return HttpResponse(request,post_context )
        return render(request, 'blog\\blog.html', post_context)



class PostDetailView(DetailView):
    model = Post
# If no template name given, then default is OBJECT. Access with OBJECT

class ConnectDetailView(DetailView):
    model = dieticians
# If no template name given, then default is OBJECT. Access with OBJECT


def bookmark(request):
    context={
        'post_list': Post.objects.all(),
        'diet_list': dieticians.objects.order_by('tot_rank_score')[::-1]
    }
    if request.method == "POST":
        if request.POST.get('deletebookmark'):
            get_id = request.POST.get('deletebookmark')
            post_row = get_object_or_404(Post, pk=get_id)
            post_row.bookmark =""
            post_row.save()
            messages.success(request, 'Bookmark Removed!')
            return render(request, 'blog\\bookmarks.html',context)
        if request.POST.get('deletecbookmark'):
            get_id = request.POST.get('deletecbookmark')
            diet_row = get_object_or_404(dieticians, pk=get_id)
            diet_row.bookmark = ""
            diet_row.save()
            messages.success(request, 'Bookmark Removed!')
            return render(request, 'blog\\bookmarks.html', context)
    else:
        return render(request, 'blog\\bookmarks.html',context)



def connect(request):
    count=0
    context = {
        'diet_list': dieticians.objects.order_by('tot_rank_score')[::-1]
    }
    for i in context['diet_list']:
        count+=1
        i.rank = count
        i.save()
    return render(request, 'blog\connect.html',context)


def post_create(request):
    global stop_words
    if request.method == "POST":
        if request.POST.get('content') and request.POST.get('title'):
            tokens1 = word_tokenize(request.POST.get('title'))
            tokens2 = word_tokenize(request.POST.get('content'))
            fault = 0
            for i in tokens1:
                if re.search('[$-_@&+#!*<>?\(\)/%]', i.lower()):
                    fault = 1

                if i.lower() in stop_words:
                    fault = 1

            for i in tokens2:
                if re.search('[$-_@&+#!*<>?\(\)/%]', i.lower()):
                    fault = 1

                if i.lower() in stop_words:
                    fault = 1

            if fault == 1:
                messages.warning(request,'We detected some policy violations | Please go through with our Terms of Usage & Chat Policy')
                return render(request, 'blog/post_form.html')
            if fault == 0:
                title = request.POST.get('title')
                content = request.POST.get('content')
                author = request.user
                data = Post(title=title, content=content, author=author)
                data.save()
                messages.success(request, 'Hurrah!!! Your Message was Posted Successfully!')
                return render(request, 'blog/post_form.html')
    else:
        return render(request, 'blog/post_form.html')

def start(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        bmi = weight / (height ** 2)
        #print("Your BMI is: {0} and you are: ".format(bmi), end='')

        # conditions
        if (bmi < 16):
            messages.warning(request, 'BMI value is '+str(bmi.__round__(2))+' You are SEVERLY UNDERWEIGHT')
        elif (bmi >= 16 and bmi < 18.5):
            messages.success(request, 'BMI value is ' + str(bmi.__round__(2)) + ' You are UNDERWEIGHT')
        elif (bmi >= 18.5 and bmi < 25):
            messages.success(request, 'BMI value is ' + str(bmi.__round__(2)) + ' You are HEALTHY')
        elif (bmi >= 25 and bmi < 30):
            messages.warning(request, 'BMI value is ' + str(bmi.__round__(2)) + ' You are OVERWEIGHT')
        else:
            messages.warning(request, 'BMI value is '+str(bmi.__round__(2))+' You are SEVERLY OVERWEIGHT')
        return render(request, 'blog/start.html')
    else:
        return render(request, 'blog/start.html')


def post_edit(request,pk):
    global stop_words
    row=get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if request.POST.get('content') and request.POST.get('title'):
            tokens1 = word_tokenize(request.POST.get('title'))
            tokens2 = word_tokenize(request.POST.get('content'))
            fault = 0
            for i in tokens1:
                if re.search('[$-_@&+#!*<>?\(\)/%]', i.lower()):
                    fault = 1

                if i.lower() in stop_words:
                    fault = 1

            for i in tokens2:
                if re.search('[$-_@&+#!*<>?\(\)/%]', i.lower()):
                    fault = 1

                if i.lower() in stop_words:
                    fault = 1

            if fault == 1:
                messages.warning(request,
                                 'We detected some policy violations | Please go through with our Terms of Usage & Chat Policy')
                return render(request, 'blog/post_form.html')
            if fault == 0:
                row.title = request.POST.get('title')
                row.content = request.POST.get('content')
                row.author = request.user
                row.save()
                messages.success(request, 'Hurrah!!! Your Post was Updated Successfully!')
                return render(request, 'blog/blog.html')
    else:
        row_context = {
        'row': get_object_or_404(Post, pk=pk)
        }
        return render(request,'blog/post_edit.html',row_context)

def post_delete(request,pk):
    if request.method == "POST":
        if request.POST.get('askconfirmation'):
            messages.warning(request, 'Do you really want to Delete this Post? Deleted pots cant be recovered!')
            context_detail={
                'object':get_object_or_404(Post, pk=pk),
                'message_trigger': 1
            }
            return render(request, 'blog/post_detail.html',context_detail)
        if request.POST.get('confirmed'):
            row = get_object_or_404(Post, pk=pk)
            row.delete()
            messages.success(request, 'Deleted Successfully')
            return render(request, 'blog/blog.html')

def app_cancel(request):
    app_context = {
        'app_list': appointments.objects.order_by('status'),
        'full_time': timezone.now(),
        'min': timezone.now().today().minute,
        'hour': timezone.now().today().hour,
        'date': timezone.now().today().date
        # 'data':data
    }
    if request.method == "POST":
        if request.POST.get('cancelapp'):
           row = get_object_or_404(appointments, pk=request.POST.get('cancelapp'))
           messages.success(request, 'Appointment CANCELLED for '+str(row.consulter))
           row.delete()
           return render(request, 'users/profile.html',app_context)


def user_actions(request,pk):
    app_context = {
        'app_list': appointments.objects.order_by('status'),
        'full_time': timezone.now(),
        'min': timezone.now().today().minute,
        'hour': timezone.now().today().hour,
        'date': timezone.now().today().date
        # 'data':data
    }
    if request.method == "POST":
        if request.POST.get('user_action') == "fulfilled":
            consulter_row = get_object_or_404(appointments, pk=pk)
            messages.success(request, 'Your requirement is already FULFILLED! This appointment will BE CLOSED')
            consulter_row.status = 'CLOSED'
            consulter_row.CLOSING = timezone.now()
            consulter_row.patient_response= 'ALREADY FULFILLED | We Request You to go ahead with consulting other patients'
            consulter_row.save()
            return render(request, 'users/profile.html', app_context)

        if request.POST.get('user_action') == "late":
            consulter_row = get_object_or_404(appointments, pk=pk)
            messages.warning(request, 'YOU ARE LATE! , So you will be putted in WAITING | Please wait until it re-opens & join SOONER as possible')
            consulter_row.status = 'WAIT'
            consulter_row.CLOSING = timezone.now()
            consulter_row.patient_response = 'Patient will be LATE to JOIN'
            consulter_row.save()
            return render(request, 'users/profile.html', app_context)

        if request.POST.get('user_action') == "Joining":
            consulter_row = get_object_or_404(appointments, pk=pk)
            id_context = {
                'id': pk
            }
            if (consulter_row.CLOSING.hour - timezone.now().today().hour) > 0:
                consulter_row.patient_response = 'Patient is JOINING | Please JOIN'
                consulter_row.save()
                return render(request, 'blog/joining.html',id_context)
            elif (consulter_row.CLOSING.minute - timezone.now().today().minute) > 1:
                consulter_row.patient_response = 'Patient is JOINING | Please JOIN'
                consulter_row.save()
                return render(request, 'blog/joining.html',id_context)
            else:
                messages.warning(request, 'ONLY'+str(consulter_row.CLOSING.second-timezone.now().today().second)+' SECONDS Left & this time is not sufficient for an appointment | Please be on-time as soon as appointment OPENs')
                messages.warning(request,'You can either mark yourself as <WILL BE LATE> or POST a new request!')
                return render(request, 'users/profile.html', app_context)

def certificate(request,pk):
    consulter_row = get_object_or_404(appointments, pk=pk)
    context={
        'row':consulter_row
    }
    return render(request, 'blog/certificate.html', context)
'''
Perfect BMI Healthy value
Weight : 65
Height ( meters ) :1.8288 | Foot : 6
'''