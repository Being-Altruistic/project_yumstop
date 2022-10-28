from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from blog.models import appointments , dieticians
#from django.http import HttpResponse
from django.utils import timezone
import django
import datetime
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Getting VALIDATED data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able login')
            return redirect('login')
    else:
        # If not a POST request. First time visit
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})

@login_required
def profile(request):
    app_context = {
        'app_list': appointments.objects.order_by('status'),
        'full_time': timezone.now(),
        'min': timezone.now().today().minute,
        'hour': timezone.now().today().hour,
        'date': timezone.now().today().date
        # 'data':data
    }
    if request.method =='POST':
        if request.POST.get('desc_box'):
            consulter_row = get_object_or_404(dieticians, pk=request.POST.get('getappointment'))
            messages.success(request, 'Appointment Request Sent! for '+str(consulter_row.name))
            consulter = consulter_row.name
            patient_id = request.user.id
            patient_name = request.user
            desc = request.POST.get('desc_box')
            status = 'WAIT'
            data = appointments(consulter=consulter, patient_id=patient_id, patient_name=patient_name, desc=desc, status=status)
            data.save()
            return render(request, 'users/profile.html',app_context)
        elif request.POST.get('leave'):
           consulter_row = get_object_or_404(appointments, pk=request.POST.get('leave'))
           consulter_row.status = 'CLOSED'
           consulter_row.CLOSING = timezone.now()
           consulter_row.save()
           messages.success(request, 'Thankyou for JOINING this meet | Come back shortly to get your treatment slip | This may take some time')
           return render(request, 'users/profile.html', app_context)
        else:
           desc_context={
               'desc_flag': 1,
               'object':get_object_or_404(dieticians, pk=request.POST.get('getappointment'))
           }
           messages.warning(request,'Please fill-in the DESCRIPTION box | More the chance to get appointment if you fill-in')
           return render(request, 'blog/dieticians_detail.html', desc_context)

    else:
        #data=str(django.utils.timezone.now)
        #data = str(timezone.now())
        #value = appointments.objects.get(consulter='Prof. Dr. Suchitra Nair')
        #print(value.CLOSING)
            #'day': timezone.now().today().minute,
            #'day': timezone.now().minute,
            #'day': django.utils.timezone.now().minute,
            #'sliced':[django.utils.timezone.now]
        #return HttpResponse(request, 'NORMAL')
        #messages.warning(request,'SKipped Post')
        return render(request, 'users/profile.html',app_context)

'''
message.debug
message.info
message.success
message.warning
message.error
'''