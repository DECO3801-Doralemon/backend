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
        forum = profile.objects.all().delete()
        response["Bio"] = request.POST["Bio"]
        project = profile(Status=response["Bio"])
        project.save()
        return HttpResponseRedirect(reverse("forum"))
    else:
		return HttpResponseRedirect("/")
