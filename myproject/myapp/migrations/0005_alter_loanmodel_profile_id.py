# Generated by Django 4.2.1 on 2023-05-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_loanmodel_amt_per_installment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanmodel',
            name='profile_id',
            field=models.EmailField(max_length=254),
        ),
    ]
