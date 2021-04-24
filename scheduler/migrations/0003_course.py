from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = ['0001_initial']

    operations = [
        migrations.CreateModel(
            name = 'Course',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Course ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]