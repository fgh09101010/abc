from djangoql.admin import DjangoQLSearchMixin
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.urls import reverse
from django.utils.html import format_html
from tickets.models import Venue, ConcertCategory, Concert, Ticket
from tickets.forms import TicketAdminForm
from import_export.admin import ImportExportActionModelAdmin



class ConcertInline(admin.TabularInline):
    model = Concert
    fields = ["name", "starts_at", "price", "tickets_left"]

    readonly_fields = ["name", "starts_at", "price", "tickets_left"]
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "capacity"]
    inlines = [ConcertInline]
    search_fields = ["name", "address", "concert__name"]
    search_help_text = "你可以搜尋場地名稱、場地位址、音樂會名稱"

@admin.register(ConcertCategory)
class ConcertCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name","concert__name"]
    search_help_text = "你可以搜音樂會種類、音樂會名稱"

class SoldOutFilter(SimpleListFilter):
    title = "Sold out"
    parameter_name = "sold_out"
    

    def lookups(self, request, model_admin):
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(tickets_left=0)
        else:
            return queryset.exclude(tickets_left=0)
@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = [
        "name", "venue", "starts_at", "tickets_left",
        "display_sold_out",  "display_price", "display_venue",
    ]
    list_select_related = ["venue"]

    def display_sold_out(self, obj):
        return obj.tickets_left == 0

    display_sold_out.short_description = "是否賣完"
    display_sold_out.boolean = True

    def display_price(self, obj):
        return f"${obj.price}"

    display_price.short_description = "門票價格"
    display_price.admin_order_field = "price"
    
    def display_venue(self, obj):
        link = reverse("admin:tickets_venue_change", args=[obj.venue.id])
        return format_html('<a href="{}">{}</a>', link, obj.venue)

    display_venue.short_description = "音樂會場地"
    list_filter = ["venue",SoldOutFilter]
    search_fields = ["name", "venue__name", "venue__address"]
    search_help_text = "你可以搜尋音樂會名稱、場地名稱、場地位址"

   

@admin.action(description="啟動所選的tickets")
def activate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="停用所選的tickets")
def deactivate_tickets(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(Ticket)
class TicketAdmin(DjangoQLSearchMixin, ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = [
        "customer_full_name", "concert",
        "payment_method", "paid_at", "is_active",
    ]
    list_select_related = ["concert", "concert__venue"]
    actions = [activate_tickets, deactivate_tickets]
    form = TicketAdminForm
    list_filter = ["concert","concert__venue"]


