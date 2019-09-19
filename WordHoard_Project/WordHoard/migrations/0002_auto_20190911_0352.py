# Generated by Django 2.2.4 on 2019-09-11 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WordHoard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='body',
        ),
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('UK', 'Unknown')], default='UK', max_length=15),
        ),
        migrations.AddField(
            model_name='text',
            name='genre',
            field=models.CharField(choices=[('P', 'Poetry'), ('F', 'Fiction'), ('NF', 'Non-Fiction')], default='F', max_length=100),
        ),
        migrations.AddField(
            model_name='text',
            name='txt_file',
            field=models.FileField(blank=True, null=True, upload_to='text_files'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='text',
            name='author',
        ),
        migrations.AddField(
            model_name='text',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='WordHoard.Author'),
        ),
        migrations.AlterField(
            model_name='text',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='translator',
            field=models.ManyToManyField(related_name='texts', to='WordHoard.Translator'),
        ),
    ]
