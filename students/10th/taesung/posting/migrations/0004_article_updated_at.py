# Generated by Django 3.0.8 on 2020-07-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_auto_20200715_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
