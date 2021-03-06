# Generated by Django 3.2.3 on 2021-05-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0005_auto_20210530_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=650, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('student', models.CharField(blank=True, max_length=250, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
