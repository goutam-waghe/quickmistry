from django.shortcuts import render , redirect
from users.models import User
from dashboard import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

def worker(request):
    user= request.user
    return render(request , "dashboard/worker_dashboard_home.html"  , {'user':user})


def worker_req(request):
     return render(request , "dashboard/worker_dashboard_req.html" )

def worker_completed(request):
     return render(request , "dashboard/worker_dashboard_completed_job.html" )

def worker_ongoing(request):
     return render(request , "dashboard/worker_dashboard_onGoing_job.html" )

def worker_deatil(request):
    user = request.user
    if request.method == "POST":
        form = forms.WorkerExtraDetailsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect("worker")
    else:
         form = forms.WorkerExtraDetailsForm(instance=user)
    return render(request , "dashboard/worker_details.html"  , {'form':form})

@login_required(login_url='/users/login/')
def profile(request):
    print(request.user)
    user = request.user
    data = {
        
    }
    if user.role == "customer":
         return render(request , "dashboard/user_profile.html"  , context=data)
    elif user.role == "worker":
         return render(request , "dashboard/worker_profile.html"  , context=data)
         
    


@login_required(login_url='/users/login/')
def customer(request):
    user = request.user
    form = forms.workerSearchForm()
    return render(request , "dashboard/user_dashboard_home.html" ,  {'user':user , "form":form})


@login_required(login_url='/users/login/')
def customer_about(request):
    user = request.user 
    return render(request , "dashboard/user_dashboard_about.html" ,  {'user':user})


def customer_service(request):
    user = request.user 
    return render(request , "dashboard/user_dashboard_service.html" ,  {'user':user})


def worker_list(request):
    form = forms.workerSearchForm(request.GET or None)
    workers = User.objects.filter(role=User.Role.WORKER, availability=True)
    if form.is_valid():
        search = form.cleaned_data.get('searchInput')
        category = form.cleaned_data.get('category')
        sort_by = form.cleaned_data.get('sort_by')
        city = form.cleaned_data.get('city')

        if search:
                workers = workers.filter(skills__icontains=search)
        if category:
                workers = workers.filter(serviceCategory=category)

        if sort_by == 'price_asc':
            workers = workers.order_by('rate')
        if city:
            workers = workers.filter(city__icontains=city)
        elif sort_by == 'price_desc':
            workers = workers.order_by('-rate')
        
    return render(request , "dashboard/list_workers_page.html" , {"workers":workers , "form":form})
    


class WorkerProfileView(DetailView):
    model = User
    template_name = "dashboard/worker_profile.html"
    context_object_name = "worker"

    def get_queryset(self):
        return User.objects.filter(role="worker")