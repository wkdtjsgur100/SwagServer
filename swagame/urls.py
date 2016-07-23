
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.user_list,name="user_list"),
	url(r'^user/',views.user_control,name="user_control"),
]
