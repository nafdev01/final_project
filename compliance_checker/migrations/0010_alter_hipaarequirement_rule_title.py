# Generated by Django 5.0.2 on 2024-02-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_checker', '0009_alter_hipaarequirement_requirement_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hipaarequirement',
            name='rule_title',
            field=models.CharField(max_length=255),
        ),
    ]
