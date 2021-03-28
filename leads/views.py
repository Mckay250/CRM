from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm



class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadUpdateView(UpdateView):
    queryset = Lead.objects.all()
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(DeleteView):
    queryset = Lead.objects.all()
    template_name = "leads/lead_delete.html"

    def get_success_url(self):
        return reverse("leads:lead-list")



def home_page(request):
    # return HttpResponse("Hello world")
    return render(request, "leads/homepage.html")


def landing_page(request):
    return render(request, "landing.html")
    

def leads_list(request):
    leads = Lead.objects.all()

    context = {
        "leads" : leads        
    }
    return render(request, "leads_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id = pk)
    context = {
        "lead" : lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        "form" : form
    }

    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance = lead)
    
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance = lead)
        if form.is_valid():
            form.save()
            return redirect(f'/leads/{pk}')

    context = {
        "form" : form,
        "lead" : lead
    }
    return render(request, "leads/lead_update.html", context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     # form = LeadModelForm()
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             first_name = cleaned_data['first_name']
#             last_name = cleaned_data['last_name']
#             age = cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect(f'/leads/{lead.id}')
#     context = {
#         "form" : form,
#         "lead" : lead
#     }
#     return render(request, "leads/lead_update.html", context)



# def lead_create(request):
#     form = LeadModelForm()
#         #  form = LeadForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         #  form = LeadForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             first_name = cleaned_data['first_name']
#             last_name = cleaned_data['last_name']
#             age = cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             return redirect('/leads')
#
#     context = {
#         "form" : form
#     }
#
#     return render(request, "leads/lead_create.html", context)