# Generated by Django 4.0.1 on 2022-01-20 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('cheatsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cheatsheet')),
            ],
        ),
    ]
