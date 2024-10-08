# Generated by Django 5.1.1 on 2024-10-01 18:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsavvy', '0004_alter_financialtip_title_notification'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_spending', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('savings_goal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('current_savings', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='FinancialTip',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
