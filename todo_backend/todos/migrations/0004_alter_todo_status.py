# Generated by Django 4.2.1 on 2023-05-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('TD', 'Todo'), ('IP', 'In-Progress'), ('DO', 'Done')], default='TD', max_length=2),
        ),
    ]
