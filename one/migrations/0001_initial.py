# Generated by Django 3.2.7 on 2021-10-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ScholarNo', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Clas', models.CharField(max_length=100)),
                ('Section', models.CharField(max_length=20)),
                ('Photo', models.ImageField(upload_to='one/images/')),
            ],
        ),
    ]
