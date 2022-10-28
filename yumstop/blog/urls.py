from django.urls import path
from .views import PostDetailView , ConnectDetailView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home', views.home, name='home'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('blog/', views.blog_part, name='blog'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/edit/<int:pk>/', views.post_edit, name='post-edit'),
    path('blog/post/delete/<int:pk>/', views.post_delete, name='post-delete'),
    path('blog/new_post/', views.post_create, name='post-create'),
    path('bookmarks/', views.bookmark, name='bookmk'),
    path('connect/', views.connect, name='connect'),
    path('connect/<int:pk>/info', ConnectDetailView.as_view(), name='top_profile'),
path('cancel/appointment/', views.app_cancel, name='app-cancel'),
    path('start', views.start, name='start'),
path('actions/<int:pk>/', views.user_actions, name='url_user_actions'),
path('your_certificate/<int:pk>/', views.certificate, name='certificate')
]

'''
blog folder name
blog in installed apps
blog in templates
blog in yumstop\ urls.py include
'''
'''
username: admin@yumstop
email : edumats100@gmail.com
pass  : yumstop@001
'''
'''
Prof.Dr.Suchitra_Nair
suchitra@gmail.com
consult@123##

Dr.Shusheel_Varma
shusheel@gmail.com
s123##**

Dr.Subender_Singh
subender@company.com
suconsult&&##


test user : 
username  : Testdiet
pass  : xyz01test

Testdiet2 
Testing231

Tejas@Shinde
tejas@gmail.com
TSuser@123

@Shevin
edumats100@gmail.com
NEW : passtest##123
nenwen newpass##123
newpass**00
newpass**123



@Shevin123
s123@gmail.com
s12300***

Testdiet3
testme@gmail.com
Diet3yumstop

NewMember
new@gmail.com
new00**123

@Newuser
user@company.com
new00com

Bala@123
user@gmail.com
B123##00

old : passtest##123
new : newpass##12300


## TEST DATA

Please guide me on how can I carry out daily workout ? My diet plans are too bad & would like to get guidance on it.

How to keep a balance between my GYM diet & regular diet?

I'm having diet in large amount. I can't avoid rice , it is must. How can I make sure that I'm having a well balanced diet? My weight is 80kg currently & feeling tired very soon after job, which was not seen earlier.

Facing obesity with weight 80kg/overweight with 90 kg
1) Do daily exercise
2) JOIN GYM if possible
3) Avoid alcohol /smoking
4) Drink 8 glasses of water 1-day
5) Avoid oily/JUNK foods
6) Eat fibrous foods
7) Pulses (Sprouted) daily 1-bowl
8) Do laughing exercise. In home it's ok.

## Possible updates
1) Credit based RANKING/BUYING
2) Download
3) Credit Pass
4) Vote Systems
5) Bulk appointments
6) Bug Report
7) Filter app with OPEN/CLOSED/WAIT
8) Filter diet with Ranks/Qualification/Field of Speciality
'''