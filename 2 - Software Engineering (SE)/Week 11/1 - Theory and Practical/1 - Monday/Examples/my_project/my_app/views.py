from django.shortcuts import render

# Create your views here.
def view_home(request):
    return render(request, 'home.html')


def welcome(request):
    name = request.POST['name']
    email = request.POST['email']
    birthday = request.POST['birthday']
    context_data = {
        'name': name,
        'email': email,
        'birthday': birthday
    }
    return render(request, 'welcome.html', context=context_data)


def sports(request):
    sports = ["rugby", "cricket", "tennis", "golf", "cycling", "netball"]
    return render(request, 'sports.html', context={'sports':sports})
