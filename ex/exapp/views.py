from django.shortcuts import render

def test(request):
    return render(request, 'content/test.html')

# Create your views here.
