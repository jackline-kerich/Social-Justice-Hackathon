# Generated by Django 5.1.1 on 2024-10-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finsavvy', '0005_userprofile_delete_financialtip_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
