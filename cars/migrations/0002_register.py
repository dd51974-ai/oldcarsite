# Generated by Django 3.1.4 on 2021-04-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('color', models.CharField(choices=[('赤', 'Red'), ('青', 'Bleu'), ('白', 'White'), ('黒', 'Black'), ('黄', 'Yellow'), ('緑', 'Green')], max_length=1, verbose_name='カラー')),
                ('shop1', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]