from django.shortcuts import render

def user_list(request):
	return render(request,'html/user_list.html',{})

# Create your views here.
