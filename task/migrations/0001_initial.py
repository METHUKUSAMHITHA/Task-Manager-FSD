# Generated by Django 3.1.7 on 2021-04-16 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completiondate', models.DateTimeField(null=True)),
                ('priority', models.BooleanField(default=False)),
                ('category',models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]