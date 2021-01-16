# Generated by Django 3.1.5 on 2021-01-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('rollno', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('std', models.IntegerField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th'), (10, '10th'), (11, '11th'), (12, '12th')], max_length=2)),
                ('city', models.CharField(max_length=10)),
            ],
        ),
    ]
