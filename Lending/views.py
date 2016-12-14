from django.shortcuts import render

def return_lending(request):
    return render(request, 'index.html')