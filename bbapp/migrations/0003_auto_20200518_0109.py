# Generated by Django 3.0.2 on 2020-05-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbapp', '0002_auto_20200518_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimages',
            name='moreImages',
            field=models.FileField(blank=True, null=True, upload_to='image/events/moreImages'),
        ),
    ]
