# Generated by Django 5.0.6 on 2024-05-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='educational_images/')),
                ('author', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('readmore', models.URLField()),
            ],
        ),
    ]