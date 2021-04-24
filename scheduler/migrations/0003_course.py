from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = ['scheduler']

    operations = [
        migrations.CreateModel(
            name = 'course',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Course ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]