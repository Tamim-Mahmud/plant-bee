from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Plant,UserInput
from .forms import UserInputForm
# Create your views here.ef PlantCreateView(request):
    

def plant_list(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserInputForm()
    user_inputs=UserInput.objects().all()
    plants = Plant.objects.create(
    name=user_inputs.name,  
    price=user_inputs.price,
    description=user_inputs.description,
    image_url=user_inputs.image_url
    )
        # Save the new Plant object
    plants.add_object(user_inputs)
    plants.save()
    plants = Plant.objects.all()
    
    # t = user_inputs.objects.filter(name=name)
    print(user_inputs[1].price)
    return render(request, 'plant/plant_list.html', {'plants' :plants , 'form' : form , 'user_inputs': user_inputs})


class PlantCreateView(CreateView):
    model = Plant
    fields = ["name","price","description","image_url"]
    