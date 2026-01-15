# Generated migration to rename post_id to product_id in Review model

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='post',
            new_name='product',
        ),
    ]
