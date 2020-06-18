# Generated by Django 3.0.5 on 2020-05-12 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0002_auto_20200512_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subrequests',
            name='user_id',
        ),
        migrations.AddField(
            model_name='subrequests',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subrequests', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subrequests',
            name='display_name',
            field=models.CharField(max_length=50, verbose_name='The name for the Subrequest'),
        ),
        migrations.CreateModel(
            name='Shifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Starting day and time')),
                ('end_time', models.DateTimeField(verbose_name='Ending day and time')),
                ('name', models.CharField(max_length=20, verbose_name='Name of shift')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]