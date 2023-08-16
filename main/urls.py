from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.index, name='index'),
    path('',views.index, name='index'),
    path('sign_up',views.sign_up, name='sign_up'),
    path('register',views.Register, name='Register'),
    path('userinfo',views.Userinfo, name='Userinfo'),
    path('news',views.News, name='news'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)