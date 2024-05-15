from django.urls import path
 
from . import views
app_name="tickets"
urlpatterns = [

    path("concert/", views.ConcertListView.as_view(), name="concert-list"),
    path("concert/<pk>/", views.ConcertDetailView.as_view(), name="concert-detail"),
    path("venue/<pk>/", views.VenueDetailView.as_view(), name="venue-detail"),
    path("buy", views.buy_ticket, name="ticket-buy"),
]