# Generated by Django 4.1.7 on 2023-05-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number_of_pages', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
