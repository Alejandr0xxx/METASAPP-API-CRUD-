# Generated by Django 5.1 on 2024-08-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('details', models.TextField()),
                ('events', models.IntegerField()),
                ('icon', models.TextField(null=True)),
                ('objective_num', models.IntegerField(null=True)),
                ('deadline', models.DateField()),
                ('completed_times', models.IntegerField(default=0)),
                ('completed_times_bef', models.IntegerField(default=0)),
                ('is_completed_bef', models.BooleanField(default=False)),
                ('frequency', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=7)),
            ],
            options={
                'db_table': 'objectives',
            },
        ),
    ]