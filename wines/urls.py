from django.urls import path
from wines.views import (
    HomeListView,
    WineListView,
    # WineCreateView,
    # WineDeleteView,
    # WineUpdateView,
    AboutView,
    contact,
    # consult,
    
)


urlpatterns = [
path("home/", HomeListView.as_view(), name="wine_home"),
path("about/", AboutView.as_view(), name="about"),
path("contact/", contact, name="contact"),
# path("consultant/", consult, name="consult"),
path("wines/", WineListView.as_view(), name="wine_list"),
# path("admin/create/", WineCreateView.as_view(), name="wine_create"),
# path("<int:pk>/delete/", WineDeleteView.as_view(), name="wine_delete"),
# path("<int:pk>/edit/", WineUpdateView.as_view(), name="wine_edit"),

# path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]