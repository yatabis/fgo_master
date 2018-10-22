# Generated by Django 2.1.2 on 2018-10-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fgo_master_app', '0008_auto_20181022_0641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noblephantasm',
            old_name='turn',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='noblephantasmeffect',
            old_name='turn',
            new_name='duration',
        ),
        migrations.AddField(
            model_name='noblephantasm',
            name='duration_type',
            field=models.CharField(blank=True, choices=[('turn', 'ターン'), ('times', '回')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='noblephantasmeffect',
            name='duration_type',
            field=models.CharField(blank=True, choices=[('turn', 'ターン'), ('times', '回')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='passiveskilleffect',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='passiveskilleffect',
            name='duration_type',
            field=models.CharField(blank=True, choices=[('turn', 'ターン'), ('times', '回')], max_length=8, null=True),
        ),
    ]