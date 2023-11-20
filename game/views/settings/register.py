from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from game.models.player.player import Player

def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confirm = data.get("password_confirm", "").strip()
    if not username or not password:
        return JsonResponse({
            'result': "empty username or password"
        })
    if password != password_confirm:
        return JsonResponse({
            'result': "password are not same"
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'result': "User exists"
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    Player.objects.create(user=user, photo="https://cloud.sbsub.com/pedia/a/a7/CHARACTER_%E7%81%B0%E5%8E%9F%E5%93%80.png")
    login(request, user)
    return JsonResponse({
        'result': "success",
    })
