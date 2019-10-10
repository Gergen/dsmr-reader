# Generated by Django 2.2.6 on 2019-10-09 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_mqtt', '0010_mqtt_gas_consumption'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jsondaytotalsmqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Day consumption: JSON'},
        ),
        migrations.AlterModelOptions(
            name='jsongasconsumptionmqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Gas consumption: JSON'},
        ),
        migrations.AlterModelOptions(
            name='jsontelegrammqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Telegram: JSON'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'default_permissions': ('delete',), 'verbose_name': 'Outgoing MQTT message', 'verbose_name_plural': 'Outgoing MQTT messages'},
        ),
        migrations.AlterModelOptions(
            name='mqttbrokersettings',
            options={'default_permissions': (), 'verbose_name': 'MQTT Broker/connection'},
        ),
        migrations.AlterModelOptions(
            name='rawtelegrammqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Telegram: Raw'},
        ),
        migrations.AlterModelOptions(
            name='splittopicdaytotalsmqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Day consumption: Split topic'},
        ),
        migrations.AlterModelOptions(
            name='splittopicgasconsumptionmqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Gas consumption: Split topic'},
        ),
        migrations.AlterModelOptions(
            name='splittopicmeterstatisticsmqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Meter Statistics: Split topic'},
        ),
        migrations.AlterModelOptions(
            name='splittopictelegrammqttsettings',
            options={'default_permissions': (), 'verbose_name': '(Data source) Telegram: Split topic'},
        ),
    ]
