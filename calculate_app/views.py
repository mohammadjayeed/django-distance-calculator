from django.shortcuts import render
from django.http import HttpResponse
from .forms import DestinationFieldForm
from .models import DistanceCalculateModel


def request_handler_calculate(request):
    if request.method == 'POST':

        form = DestinationFieldForm(request.POST or None)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.location = "Somewhere"
            instance.destination = form.cleaned_data.get('destination')
            instance.distance = 5000.00
            instance.save()

        obj = DistanceCalculateModel.objects.all()
        print(obj)

        return HttpResponse({"done"})


    else:

        return render(request, 'main_app_template.html',{'hi':'hi'})