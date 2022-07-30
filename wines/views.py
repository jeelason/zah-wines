from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from wines.forms import ContactForm, ConsultForm
from wines.models import Wine


class HomeListView(ListView):
    model = Wine
    template_name = "wines/home.html"

class WineListView(ListView):
    model = Wine
    template_name = "wines/wines.html"

class WineCreateView(LoginRequiredMixin, CreateView):
    model = Wine
    template_name = "admin/create.html"
    fields = "__all__"
    success_url = reverse_lazy("wine_list")

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class WineDeleteView(LoginRequiredMixin, DeleteView):
    model = Wine
    template_name = "admin/delete.html"
    fields = "__all__"
    success_url = reverse_lazy("wine_list")

class WineUpdateView(LoginRequiredMixin, UpdateView):
    model = Wine
    template_name = "admin/edit.html"
    fields = "__all__"
    success_url = reverse_lazy("wine_list")


class AboutView(ListView):
    model = Wine
    template_name = "wines/about.html"
    
def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True        
        return render(request, 'wines/contact.html',{'form': form, 'submitted': submitted})


def consult(request):
    submitted = False
    if request.method == "POST":
        form = ConsultForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ConsultForm()
        if 'submitted' in request.GET:
            submitted = True        
        return render(request, 'wines/consult.html',{'form': form, 'submitted': submitted})

