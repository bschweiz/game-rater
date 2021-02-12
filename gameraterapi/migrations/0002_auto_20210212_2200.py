# Generated by Django 3.1.6 on 2021-02-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameraterapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamecategory',
            name='content',
        ),
        migrations.AddField(
            model_name='gamecategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gameraterapi.category'),
            preserve_default=False,
        ),
    ]
