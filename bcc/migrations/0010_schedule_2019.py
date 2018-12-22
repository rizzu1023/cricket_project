# Generated by Django 2.1.3 on 2018-12-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcc', '0009_auto_20181221_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule_2019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_1', models.CharField(max_length=40)),
                ('team_2', models.CharField(max_length=40)),
                ('tournament', models.CharField(default='Balapeer Cricket Tournament 2019', max_length=40)),
                ('dates', models.DateField()),
                ('times', models.TimeField()),
                ('match_id', models.ForeignKey(on_delete='models.CASCADE', to='bcc.Team')),
            ],
        ),
    ]
