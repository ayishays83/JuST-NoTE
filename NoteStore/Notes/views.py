from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Note
# from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'frotend/index.html')

def Register(request):
    form=UserCreationForm()

    if request.method == "POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account Created successfully")
            return redirect('Notes:login')


    context={
        'form':form
    }
    return render(request,'frotend/register.html',context)


def Logged(request):
    notes=Note.objects.all()
    context={
        'notes':notes
    }
    return render(request,'frotend/note.html',context)


def logout(request):
    return render(request,'frotend/logout.html')