from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('albums/',views.albums,name='albums'),
    path('commingsoon/',views.comingsoon1,name='comingsoon1'),
    path('contact/',views.contact4,name='contact4'),
    path('events/',views.events,name='events'),
    path('faq/',views.faq,name='faq'),
    path('gallary/',views.gallery1,name='gallery1'),
    path('shopregister/',views.shopregister,name='shopregister'),
    path('shop/',views.shop,name='shop'),
    path('singlealbum/',views.singlealbum,name='singlealbum'),
    path('team/',views.team,name='team'),
    path('teamsingle/',views.teamsingle,name='teamsingle'),
    path('about/',views.about,name='about'),
    path('shopproduct<int:pk>/',views.shopproduct,name='shopproduct'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot-password-page'),
    path('send-otp/', views.send_otp, name='send-otp'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('userlist/',views.userlist,name='userlist'),
    path('ver_user<int:pk>/',views.ver_user,name='ver_user'),
    path('newsletter/',views.newsletter,name='newsletter'),
   
]