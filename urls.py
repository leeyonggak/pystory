from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('develop',views.develop,name='develop'),
	path('question',views.question,name='question')
]