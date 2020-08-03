from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"form.html")
def disp(request):
   # info=[request.POST.get("First Name"),request.POST.get("Last Name"),request.POST.get("Email Id"),int(request.POST.get("Mobile No"))]
    info={
        "First Name":request.POST.get("First Name"),
        "Last Name":request.POST.get("Last Name"),
    }