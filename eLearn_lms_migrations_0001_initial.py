# Generated by Django 3.0.4 on 2020-07-08 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30, null=True)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('specialization', models.CharField(max_length=255)),
                ('teaching_method', models.TextField()),
                ('video_link', models.CharField(blank=True, max_length=255, null=True)),
                ('email_id', models.EmailField(max_length=50, null=True)),
                ('mobile_no', models.CharField(max_length=10)),
                ('address', models.TextField(null=True)),
                ('resume', models.FileField(upload_to='documents/')),
                ('applied_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.District')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('education', models.CharField(choices=[('S', 'School'), ('C', 'College')], max_length=1, null=True)),
                ('institution', models.CharField(blank=True, max_length=200, null=True)),
                ('board', models.CharField(blank=True, choices=[('S', 'State Board'), ('C', 'CBSE'), ('I', 'ICSE')], max_length=1, null=True)),
                ('grade', models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], max_length=4, null=True)),
                ('year', models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V')], max_length=3, null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.District')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
