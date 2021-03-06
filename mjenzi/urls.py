from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name = 'home'),
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('post/',views.post, name='post'),
    path('update_profile/',views.update_profile, name='update_profile'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
