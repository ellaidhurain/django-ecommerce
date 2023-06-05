# Generated by Django 4.1.4 on 2023-01-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_order_quantity_productdata_product_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerdata',
            options={'ordering': ('Date_of_join',)},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('CreatedDate',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('CreatedDate',), 'permissions': (('can_view_post', 'customer_can_view_post'), ('can_change_post', 'customer_can_change_post'))},
        ),
        migrations.AlterModelOptions(
            name='productdata',
            options={'ordering': ('CreatedDate',)},
        ),
        migrations.AlterField(
            model_name='productdata',
            name='Product_image',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to='product_pics'),
        ),
    ]
