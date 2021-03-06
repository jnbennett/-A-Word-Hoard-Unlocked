# Generated by Django 2.0.13 on 2019-09-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordHoard', '0004_auto_20190927_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='time_period',
            field=models.CharField(choices=[('CLS', 'The Classical Period (1200 BCE-455 CE)'), ('MED', 'The Medieval Period (455-1485 CE)'), ('REN', 'The Renaissance and Reformation (1485-1660)'), ('ENL', 'The Englightenment (1660-1790)'), ('ROM', 'The Romantic Period (1790-1830)'), ('VIC', 'The Victorian Period (1832-1901'), ('MOD', 'The Modern Period (1914-1945)'), ('PM', 'The PostModern Period (1945-Present Day)'), ('UNK', 'Unknown')], default='UNK', max_length=50),
        ),
    ]
