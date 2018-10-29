# Generated by Django 2.1.2 on 2018-10-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fgo_master_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servant',
            old_name='base_ATK',
            new_name='ATK1',
        ),
        migrations.RenameField(
            model_name='servant',
            old_name='base_HP',
            new_name='ATK10',
        ),
        migrations.RenameField(
            model_name='servant',
            old_name='max_ATK',
            new_name='ATK100',
        ),
        migrations.RenameField(
            model_name='servant',
            old_name='max_HP',
            new_name='ATK20',
        ),
        migrations.RenameField(
            model_name='servant',
            old_name='palingenesis_ATK',
            new_name='ATK30',
        ),
        migrations.RenameField(
            model_name='servant',
            old_name='palingenesis_HP',
            new_name='ATK40',
        ),
        migrations.RemoveField(
            model_name='servant',
            name='id',
        ),
        migrations.AddField(
            model_name='servant',
            name='ATK50',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='ATK60',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='ATK70',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='ATK80',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='ATK90',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP100',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP20',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP30',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP40',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP50',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP60',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP70',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP80',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='HP90',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='agl',
            field=models.CharField(default='A', max_length=4),
        ),
        migrations.AddField(
            model_name='servant',
            name='cv',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='servant',
            name='end',
            field=models.CharField(default='A', max_length=4),
        ),
        migrations.AddField(
            model_name='servant',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servant',
            name='illust',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='servant',
            name='luk',
            field=models.CharField(default='A', max_length=4),
        ),
        migrations.AddField(
            model_name='servant',
            name='mp',
            field=models.CharField(default='A', max_length=4),
        ),
        migrations.AddField(
            model_name='servant',
            name='np',
            field=models.CharField(default='A', max_length=4),
        ),
        migrations.AddField(
            model_name='servant',
            name='origin',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='servant',
            name='region',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='servant',
            name='str',
            field=models.CharField(default='A', max_length=4),
        ),
        migrations.AddField(
            model_name='servant',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='servant',
            name='No',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
