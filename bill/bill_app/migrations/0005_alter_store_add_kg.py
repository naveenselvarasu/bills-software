# Generated by Django 3.2.8 on 2022-05-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0004_auto_20220516_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_add',
            name='kg',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
