from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = ['0001_initial']

    operations = [
        migrations.CreateModel(
            name = 'User',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='User ID')),
                ('role', models.IntegerField(verbose_name='User Role')),
                ('name', models.CharField(max_length=30, verbose_name='Full Name')),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]