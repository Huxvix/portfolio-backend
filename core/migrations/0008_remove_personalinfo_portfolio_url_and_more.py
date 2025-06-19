
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_skill_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='portfolio_url',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='twitter_url',
        ),
    ]
