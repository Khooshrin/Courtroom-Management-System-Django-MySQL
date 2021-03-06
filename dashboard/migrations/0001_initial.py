# Generated by Django 4.0.4 on 2022-04-20 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Name', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('ContactNo', models.IntegerField()),
                ('City', models.CharField(max_length=45)),
                ('Street', models.CharField(max_length=45)),
                ('Pincode', models.IntegerField()),
                ('NoOfCases', models.IntegerField(default=0)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('Name', models.CharField(max_length=45)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('ContactNo', models.IntegerField()),
                ('YearsOfExp', models.IntegerField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('Name', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('ContactNo', models.IntegerField()),
                ('WorkExperience', models.IntegerField()),
                ('SuccessRate', models.IntegerField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer_Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(max_length=45)),
                ('LawyerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.lawyer')),
            ],
        ),
        migrations.CreateModel(
            name='Client_Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DependentName', models.CharField(max_length=45)),
                ('ClientEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='LawyerEmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.lawyer'),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('CaseID', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('CaseType', models.CharField(max_length=45)),
                ('CaseInfo', models.CharField(max_length=45)),
                ('JudgeID', models.IntegerField()),
                ('Verdict', models.CharField(max_length=45)),
                ('DefenseLawyerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DefenseLawyer', to='dashboard.lawyer')),
                ('ProsecutorLawyerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProsecutorLawyer', to='dashboard.lawyer')),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('CaseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dashboard.case')),
                ('EvidenceInfo', models.CharField(max_length=100)),
                ('JudgeEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.judge')),
                ('LawyerEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.lawyer')),
            ],
        ),
        migrations.AddConstraint(
            model_name='case',
            constraint=models.UniqueConstraint(fields=('DefenseLawyerEmail', 'ProsecutorLawyerEmail'), name='two_diff_lawyers'),
        ),
        migrations.AddConstraint(
            model_name='evidence',
            constraint=models.UniqueConstraint(fields=('CaseID', 'LawyerEmail'), name='evidence_lawyer_case'),
        ),
    ]
