# Generated by Django 3.1.2 on 2020-10-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_backup', '0011_remove_backupsettings_latest_backup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropboxsettings',
            name='access_token',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Dropbox access token'),
        ),
    ]