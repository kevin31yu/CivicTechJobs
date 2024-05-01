# Generated by Django 4.2.4 on 2024-04-27 00:15

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_opportunityxmeetings_opportunityxtech_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=255)),
                ('subrole', models.CharField(max_length=255)),
                ('project', models.CharField(max_length=255)),
                ('meetings_times', models.JSONField(default=list)),
                ('difficulty_level', models.IntegerField()),
                ('details', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by_or_token', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
