# Generated by Django 5.0.2 on 2024-02-19 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_checker', '0005_rename_rule_description_hipaarule_rule_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HIPAARule',
            new_name='HIPAARequirement',
        ),
    ]
