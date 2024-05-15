from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .drawing import *
from .forms import ticketsForm
from django.views.generic import DetailView,ListView


class ConcertListView(ListView):
    model = Concert
    template_name = 'concert.html'
    queryset = Concert.objects.order_by('starts_at')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        starts_at_list = [concert.starts_at for concert in context['object_list']]
        name_list = [concert.name for concert in context['object_list']]
        ticket_left_list = [concert.tickets_left for concert in context['object_list']]
        ticket_price_list = [concert.price for concert in context['object_list']]
        venue_names = [concert.venue.name for concert in context['object_list']]
    
        time_axis = generate_time_axis(starts_at_list,name_list,ticket_left_list)
        price=generate_price(name_list,ticket_price_list)
        context['time_axis'] = time_axis
        context["price"]=price
        context['venue_names'] = venue_names


        return context

class ConcertDetailView(DetailView):
    model = Concert
    template_name = 'detail.html'
    # context_object_name = 'abc' 預設concert_list

class VenueDetailView(DetailView):
    model = Venue
    template_name = 'venue_detail.html'
    # context_object_name = 'abc' 預設concert_list

def buy_ticket(request):
    form = ticketsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return render(request, "buy.html", context)