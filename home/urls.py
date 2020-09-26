from django.urls import path

from . import views

app_name = "home"
 
urlpatterns = [ 

    path('', views.landing, name='landing'),

    path('about/', views.about, name='about'),
    path('websites/', views.websites, name='websites'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contactSuccess, name='contactSuccess'),
    
    # path('privacy_policy/',views.private_policy, name='privacy_policy'),
    # path('terms-of-use/',views.terms_of_use, name='terms_of_use'),
    # path('disclaimer/',views.disclaimer, name='disclaimer'),
    # path('copyright/',views.copyright, name='copyright'),
    
    # path('redirect/http/', views.redirectHTTP, name="redirectHTTP"),

    # path('robots.txt',views.robots, name='robots'),
   
]