# Generated by Django 3.0.5 on 2020-07-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0047_auto_20200729_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappointments',
            name='apPhone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
