# Generated by Django 5.0.2 on 2024-02-16 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['business_name'], 'verbose_name_plural': 'Companies'},
        ),
        migrations.RenameField(
            model_name='business',
            old_name='company_address',
            new_name='business_address',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='company_name',
            new_name='business_name',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='company_phone',
            new_name='business_phone',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='company_website',
            new_name='business_website',
        ),
    ]
