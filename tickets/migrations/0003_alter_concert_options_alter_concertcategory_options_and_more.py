# Generated by Django 4.2.4 on 2024-05-12 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_concert_options_alter_concertcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concert',
            options={'ordering': ['starts_at'], 'verbose_name': '音樂會', 'verbose_name_plural': '音樂會'},
        ),
        migrations.AlterModelOptions(
            name='concertcategory',
            options={'ordering': ['name'], 'verbose_name': '音樂會種類', 'verbose_name_plural': '種類'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': '音樂會門票', 'verbose_name_plural': '門票'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'verbose_name': '音樂會場地', 'verbose_name_plural': '場地'},
        ),
        migrations.AlterField(
            model_name='concert',
            name='name',
            field=models.CharField(max_length=64, verbose_name='音樂會名稱'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='門票價格'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='starts_at',
            field=models.DateTimeField(verbose_name='開始時間'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='tickets_left',
            field=models.IntegerField(default=0, verbose_name='剩餘門票'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.venue', verbose_name='音樂會場地'),
        ),
        migrations.AlterField(
            model_name='concertcategory',
            name='name',
            field=models.CharField(max_length=64, verbose_name='音樂會類別'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='concert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.concert', verbose_name='音樂會'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer_full_name',
            field=models.CharField(max_length=64, verbose_name='顧客全名'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='有動作'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='paid_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='付款日期'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('CC', 'Credit card'), ('DC', 'Debit card'), ('ET', 'Ethereum'), ('BC', 'Bitcoin')], default='CC', max_length=2, verbose_name='付款方式'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=256, unique=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.PositiveIntegerField(verbose_name='可容納人數'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=64, verbose_name='場地名稱'),
        ),
    ]
