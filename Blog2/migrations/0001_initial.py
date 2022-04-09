# Generated by Django 3.2.7 on 2021-09-14 12:06

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='upload/blog2/blogcatImg/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='upload/blog/postImg/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_to', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog2.blogcategory')),
            ],
        ),
    ]
