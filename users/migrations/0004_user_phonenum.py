# Generated by Django 3.2.12 on 2022-02-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profileimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phonenum',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]