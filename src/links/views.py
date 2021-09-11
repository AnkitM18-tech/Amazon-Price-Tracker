from .forms import AddLinkForm
from .models import Link
from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.
'''
For our home view we need to pass to the template:
-query set(qs)
-number of items
-number of items discounted
-form
-error if any

'''
def home_view(request):
    no_of_discounted = 0
    error = None
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Oops...couldn't get the name or price!"
        except:
            error = "Oops...something went wrong!"
    form = AddLinkForm()

    qs = Link.objects.all()
    no_of_items = qs.count()
    if no_of_items > 0:
        discounted_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discounted_list.append(item)
            no_of_discounted = len(discounted_list)

    context ={
        'qs':qs,
        'no_of_items':no_of_items,
        'no_of_discounted':no_of_discounted,
        'form':form,
        'error':error,
    }

    return render(request, 'links/main.html', context)
    
class LinkDeleteView(DeleteView):
    model = Link
    template_name = "links/confirm_delete.html"
    success_url = reverse_lazy("home")

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')