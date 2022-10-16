from django.urls import include, path
from mypolls.views import IndexView, AboutView

app_name = 'mypolls' # Important

urlpatterns = [
    path('', IndexView.as_view(),  name='index'),
    path('about', AboutView.as_view(),  name='about'),

]