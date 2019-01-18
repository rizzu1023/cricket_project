# Generated by Django 2.1.3 on 2018-12-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcc', '0014_player_info_player_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='batting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bt_matches', models.IntegerField(verbose_name=7)),
                ('Bt_runs', models.IntegerField(default=300)),
                ('Bt_balls', models.IntegerField(default=234)),
                ('Bt_innings', models.IntegerField(default=5)),
                ('Bt_fours', models.ImageField(default=14, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='player_info',
            name='player_role',
            field=models.CharField(choices=[('Batsman', 'BATSMAN'), ('Bowler', 'BOWLER'), ('WicketKeeper', 'WICKET-KEEPER'), ('AllRounder', 'ALL-ROUNDER')], default='Batsman', max_length=30),
        ),
        migrations.AddField(
            model_name='batting',
            name='player_id',
            field=models.ForeignKey(on_delete='models.CASCADE', to='bcc.player_info'),
        ),
    ]