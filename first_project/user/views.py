from django.shortcuts import render
from user.forms import SigninForm
# Create your views here.
def welcome(request):
    return render(request, 'user/welcome.html')

def SigninView(request):
    form = SigninForm()
    if request.method =='POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return welcome(request)

        else:
            print('ERROR FROM INVALID')

    return render(request, 'user/signin.html', {'form':form})
