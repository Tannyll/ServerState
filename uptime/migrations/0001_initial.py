# Generated by Django 2.2 on 2019-04-09 09:49

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
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('interval', models.PositiveSmallIntegerField(choices=[(300, '5 minutes'), (1800, 'Half an hour'), (3600, '1 hour'), (21600, '6 hours')], default=1800, verbose_name='Monitoring interval')),
                ('status', models.CharField(blank=True, choices=[('online', 'Online'), ('offline', 'Offline')], max_length=9, verbose_name='Status')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Is active?')),
                ('checked_at', models.DateTimeField(editable=False, null=True, verbose_name='Checked at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monitors', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Monitor',
                'verbose_name_plural': 'Monitors',
                'ordering': ('-created_at',),
                'unique_together': {('user', 'url')},
            },
        ),
    ]
