from django.db import models


class Venue(models.Model):
    name = models.CharField(verbose_name="場地名稱",max_length=64)
    description = models.TextField(max_length=256, blank=True, null=True)
    address = models.CharField(verbose_name="地址",max_length=256, unique=True)
    capacity = models.PositiveIntegerField(verbose_name="可容納人數")
    class Meta:
        verbose_name = "音樂會場地"
        verbose_name_plural = "場地"
    def __str__(self):
        return f"{self.name}"


class ConcertCategory(models.Model):
    name = models.CharField(verbose_name="音樂會類別",max_length=64)
    description = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = "音樂會種類"
        verbose_name_plural = "種類"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Concert(models.Model):
    name = models.CharField(verbose_name="音樂會名稱",max_length=64)
    description = models.TextField(max_length=256, blank=True, null=True)
    categories = models.ManyToManyField(ConcertCategory)
    venue = models.ForeignKey(verbose_name="音樂會場地",to=Venue, on_delete=models.SET_NULL, null=True)
    starts_at = models.DateTimeField(verbose_name="開始時間")
    price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="門票價格")
    tickets_left = models.IntegerField(verbose_name="剩餘門票",default=0)

    class Meta:
        verbose_name = "音樂會"
        verbose_name_plural = "音樂會"
        ordering = ["starts_at"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id is None:
            self.tickets_left = self.venue.capacity

        super().save(force_insert, force_update, using, update_fields)

    def is_sold_out(self):
        return self.tickets_left == 0

    def __str__(self):
        return f"{self.name}"


class Ticket(models.Model):
    concert = models.ForeignKey(verbose_name="音樂會",to=Concert, on_delete=models.CASCADE)
    customer_full_name = models.CharField(verbose_name="顧客全名",max_length=64)
    PAYMENT_METHODS = [
        ("CC", "Credit card"),
        ("DC", "Debit card"),
        ("ET", "Ethereum"),
        ("BC", "Bitcoin"),
    ]
    payment_method = models.CharField(verbose_name="付款方式",
        max_length=2, default="CC", choices=PAYMENT_METHODS
    )
    paid_at = models.DateTimeField(verbose_name="付款日期",auto_now_add=True)
    is_active = models.BooleanField(verbose_name="是否生效",default=True)
    class Meta:
        verbose_name = "音樂會門票"
        verbose_name_plural = "門票"
    def __str__(self):
        return f"{self.customer_full_name}"
