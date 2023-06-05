# Generated by Django 4.1.4 on 2023-01-21 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_post_options_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='productdata',
            name='Product_image',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='productdata',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('zipcode', models.CharField(max_length=200, null=True)),
                ('CreatedDate', models.DateField(auto_now_add=True, null=True)),
                ('customer_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.customerdata')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.order')),
            ],
        ),
    ]
