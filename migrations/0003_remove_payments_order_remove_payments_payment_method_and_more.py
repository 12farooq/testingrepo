# Generated by Django 4.2.4 on 2023-10-28 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blogsidebar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='order',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='payment_method',
        ),
        migrations.DeleteModel(
            name='PaymentMethods',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
