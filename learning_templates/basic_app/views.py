from django.shortcuts import render

def index(request):
    context = {
        'name' : 'Nafiz',
        'roll' : 7,
    }
    return render(request,'basic_app/index.html',context)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative.html')



