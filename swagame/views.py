from django.shortcuts import render
from .models import Login
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import QueryDict

def exist_check_user(request):
	return Login.objects.filter(user_id=request.POST['user_id']).count() != 0

@csrf_exempt
def user_list(request):
	rank_list = Login.objects.all().order_by('user_score')
	
	datas = serializers.serialize('json',rank_list)
	encoded_result = datas.encode('utf-8')
	return JsonResponse(encoded_result,safe=False)

@csrf_exempt
def user_insert(request):
	if not exist_check_user(request):
                ins = Login(user_id=request.POST['user_id'],user_nickname=request.POST['user_nickname'],user_score=0,user_signin_time=timezone.now())
                ins.save()
                return JsonResponse({"result_msg":"ok"})
        else:
                return JsonResponse({"result_msg":"already_exist"})

@csrf_exempt
def update_userscore(request):	
	put = QueryDict(request.body)
	user = Login.objects.get(user_id=put.get('user_id'))
	if not user is None:
		user.user_score = put.get('user_score')
		user.save()
		return JsonResponse({"result_msg":"ok"})

@csrf_exempt
def user_control(request):
	if request.method == 'POST':
		return user_insert(request)

	#update score..
	elif request.method == 'PUT':		
		return update_userscore(request)
	elif request.method == 'GET':
		return user_list(request)
	else:
		return JsonResponse({"result_msg":"cannot find request method"})

# Create your views here.
