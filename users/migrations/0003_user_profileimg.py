# Generated by Django 3.2.12 on 2022-02-20 21:30

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileimg',
            field=models.ImageField(default=0, upload_to=users.models.get_file_path),
        ),
    ]