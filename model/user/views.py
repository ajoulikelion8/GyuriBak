from django.shortcuts import render
from user.models import User
# Create your views here.
def index(request):
    user_list = User.objects.all()
    return render(request,'user/index.html',{'user' : user_list})

