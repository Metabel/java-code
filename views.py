from django.shortcuts import render

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        #save to database
        contact.objects.create(name=name ,email=email, message=message)
        
    return render(request,'contact.html')
   

# Create your views here.
