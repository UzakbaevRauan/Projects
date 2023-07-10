# Generated by Django 3.2.16 on 2023-07-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('job_title', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('birthday', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
    ]