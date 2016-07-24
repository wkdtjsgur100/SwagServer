from django.shortcuts import render
from .models import Login
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import QueryDict

def exist_check_user(request):
	return Login.objects.filter(user_id=request.POST['user_id']).count() != 0

@csrf_exempt
def user_list(request):
	rank_list = Login.objects.order_by('-user_score')
	
	datas = serializers.serialize('json',rank_list,fields=('user_id','user_nickname','user_score'))
	encoded_result = datas.encode('utf-8')
	return HttpResponse(encoded_result)

@csrf_exempt
def user_insert(request):
	if not exist_check_user(request):
                ins = Login(user_id=request.POST['user_id'],user_nickname=request.POST['user_nickname'],user_score=0,user_signin_time=timezone.now())
                ins.save()
                return JsonResponse({"result_msg":"ok"})
        else:
                return JsonResponse({"result_msg":"already_exist"})

@csrf_exempt
def update_userinfo(request):	
	put = QueryDict(request.body)
	user = Login.objects.get(user_id=put.get('user_id'))
	if not user is None:
		if put.get('update_type') == '1':
			if int(user.user_score) < int(put.get('user_score')):
				user.user_score = put.get('user_score')
		elif put.get('update_type') == '2':
			user.connect_time = timezone.now()
		elif put.get('update_type') == '3':
			user.shutgame_time = timezone.now()
		else:
			return JsonResponse({"result_msg":put.get('update_type')})

		user.save()

		return JsonResponse({"result_msg":"ok"})
	else:
		return JsonResponse({"result_msg":"user is None"})
@csrf_exempt
def update_connectTime(request):
	put = QueryDict(request.body)
	
@csrf_exempt
def user_control(request):
	if request.method == 'POST':
		return user_insert(request)

	#update score..
	elif request.method == 'PUT':	
		return update_userinfo(request)

	elif request.method == 'GET':
		return user_list(request)
	else:
		return JsonResponse({"result_msg":"cannot find request method"})

# Create your views here.
