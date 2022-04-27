# Generated by Django 4.0.4 on 2022-04-23 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_case_defenselawyeremail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='JudgeID',
        ),
        migrations.AddField(
            model_name='case',
            name='JudgeEmail',
            field=models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard.judge'),
        ),
    ]