# Generated by Django 5.0.2 on 2024-02-19 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compliance_checker', '0010_alter_hipaarequirement_rule_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hipaachecklistitem',
            name='checklist_number',
        ),
    ]