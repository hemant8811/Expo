# Generated by Django 4.0.4 on 2022-07-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
