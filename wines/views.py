from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from wines.forms import ContactForm, ConsultForm
from wines.models import Consultant, Contact, Wine, Task


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

class InquiriesListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "admin/inquiries.html"
    context_object_name = 'contacts_list'
    queryset = Contact.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InquiriesListView, self).get_context_data(**kwargs)
        context['consultants_list'] = Consultant.objects.all()
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "admin/complete.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("inquiries")


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            return HttpResponseRedirect("?submitted=True")
    else:
        form = ContactForm()
        if "submitted" in request.GET:
            submitted = True
        return render(
            request, "wines/contact.html", {"form": form, "submitted": submitted}
        )


def consult(request):
    submitted = False
    if request.method == "POST":
        form = ConsultForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            return HttpResponseRedirect("?submitted=True")
    else:
        form = ConsultForm()
        if "submitted" in request.GET:
            submitted = True
        return render(
            request, "wines/consult.html", {"form": form, "submitted": submitted}
        )
