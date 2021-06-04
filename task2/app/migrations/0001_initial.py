# Generated by Django 3.2.4 on 2021-06-03 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('batsmen', 'batsmen'), ('bowler', 'bowler'), ('keeper', 'keeper')], max_length=100)),
                ('batting', models.IntegerField(max_length=10)),
                ('bowling', models.IntegerField(max_length=10)),
                ('batsmen', models.BooleanField(default=False)),
                ('bowler', models.BooleanField(default=False)),
                ('keeper', models.BooleanField(default=False)),
            ],
        ),
    ]
