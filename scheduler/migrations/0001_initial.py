from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name = 'Administrator',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Full Name')),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
    ]