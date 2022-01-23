# Generated by Django 2.2.7 on 2019-11-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
