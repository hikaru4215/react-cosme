# Generated by Django 2.2.17 on 2021-01-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosme', '0002_recommenditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.CharField(max_length=50, verbose_name='おすすめ度')),
            ],
        ),
    ]
