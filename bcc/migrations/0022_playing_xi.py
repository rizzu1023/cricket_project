# Generated by Django 2.1.3 on 2019-01-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcc', '0021_auto_20181227_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='playing_XI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.CharField(choices=[('VK', 'Virat Kohli'), ('ST', 'Sachin'), ('RS', 'Rohit Sharma'), ('MS', 'Mohammed Shami')], max_length=100)),
            ],
        ),
    ]
