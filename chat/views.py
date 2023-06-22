from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import time
import os

uid = 1


def get_token(request):
    global uid
    uid += 1
    app_id = os.getenv('APP_ID')
    app_certificate = os.getenv('APP_CERTIFICATE')
    channel_name = 'main'
    expiration_time_in_secs = 3600 * 24
    current_time = time.time()
    privilege_expired_time = current_time + expiration_time_in_secs
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(app_id, app_certificate, channel_name, uid, role, privilege_expired_time)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)


def get_app_id(request):
    app_id = os.getenv("APP_ID")
    return JsonResponse({'app_id': app_id})


def chat(request):
    return render(request, 'chat.html')


def join(request):
    return render(request, 'join.html', {'video_chat_page': True})
