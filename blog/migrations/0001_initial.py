# Generated by Django 3.2.7 on 2021-11-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]