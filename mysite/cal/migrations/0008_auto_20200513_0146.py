# Generated by Django 3.0.5 on 2020-05-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0007_auto_20200513_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subrequests',
            name='anonymous',
            field=models.BooleanField(blank=True, default=True, verbose_name='Whether or not you want your request to be anonymous'),
        ),
    ]