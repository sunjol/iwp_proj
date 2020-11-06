from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from account.models import Account

# Create your views here.
app_name='chat'

def index(request):
	return render(request, 'chat/room.html',{
        'username':mark_safe(json.dumps(request.user.username)),
        'accountss':Account.objects.all(),
        'pk':mark_safe(json.dumps(request.user.my_id))

    
    })
def room(request, room_name):
	# context={}
	# context['room_name_json']=mark_safe(json.dumps(room_name))
	# context['accounts']=Account.objects.all()
	# context['username']=mark_safe(json.dumps(request.user.username))
    return render(request, 'chat/room.html',{
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username':mark_safe(json.dumps(request.user.username)),
        'accountss':Account.objects.all(),
        'pk':mark_safe(json.dumps(request.user.my_id))
    
    })