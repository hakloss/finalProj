from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('0004_course', '0001_initial'),]

    operations = [
        migrations.CreateModel(
            name = 'Lab',
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Section ID')),
                ('number', models.IntegerField()),
            ],
        ),
    ]