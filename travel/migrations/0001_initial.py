# Generated by Django 4.0.4 on 2022-05-20 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='cities/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('available_display', models.BooleanField(default=True, verbose_name='Display')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='travel.category')),
            ],
            options={
                'ordering': ['-created'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]
