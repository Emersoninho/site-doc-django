# Generated by Django 5.1.4 on 2025-01-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='imagem',
            field=models.FileField(blank=True, default=None, null=True, upload_to='images/user'),
        ),
    ]
