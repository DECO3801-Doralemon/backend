from django.shortcuts import render
from .models import profile, wasteStats
from .forms import changeBioForm

response={}

def changeBioForm(request):
    response["changeBioForm"] = changeBioForm()
    return render(request, "changeBioForm", response)

def replaceBio(request):
    form = changeBioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        #temp needs to be changed to view that directs to profile html
        temp = profile.objects.all().delete()
        response["Bio"] = request.POST["Bio"]
        project = profile(Status=response["Bio"])
        project.save()
        return HttpResponseRedirect(reverse("<Change to view that directs to profile html>"))
    else:
        return HttpResponseRedirect("/")
