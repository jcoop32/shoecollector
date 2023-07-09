# Generated by Django 4.2.3 on 2023-07-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_shoe_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='type',
            field=models.CharField(choices=[('B', 'Boots'), ('S', 'Sneakers'), ('C', 'Casual'), ('A', 'Athletic')], default='S', max_length=50),
        ),
    ]