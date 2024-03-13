from django.shortcuts import render

# Create your views here.
people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
    return render(request, 'my_form/add.html')

def list_people(request):
    return render(request, 'my_form/list.html', {'people': people})

