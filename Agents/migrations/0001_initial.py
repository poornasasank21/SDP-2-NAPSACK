# Generated by Django 4.0.2 on 2022-04-26 11:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('NapsackAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentOrders',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('pincode', models.PositiveIntegerField()),
                ('locality', models.TextField()),
                ('address', models.TextField()),
                ('city_district_town', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('agent_order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bill', models.CharField(max_length=100)),
                ('delivery_info', models.TextField()),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_date', models.DateTimeField()),
                ('delivery_status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AgentsUsers',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('agen_user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('agent_shop_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('agent_shop_name', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AgentLocation',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Agents.agentsusers')),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AgentsAddress',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Agents.agentsusers')),
                ('phone_number', models.PositiveIntegerField()),
                ('pincode', models.PositiveIntegerField()),
                ('locality', models.TextField()),
                ('address', models.TextField()),
                ('city_district_town', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AgentProductsCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Categories_name', models.CharField(max_length=300)),
                ('agent_shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agents.agentsusers')),
                ('product_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NapsackAdmin.productscategories')),
            ],
        ),
        migrations.CreateModel(
            name='AgentProducts',
            fields=[
                ('agent_product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
                ('offer', models.IntegerField()),
                ('quantity_present', models.IntegerField()),
                ('agentsusers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agents.agentsusers')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agents.agentproductscategories')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NapsackAdmin.products')),
            ],
        ),
        migrations.CreateModel(
            name='AgentOrdersProducts',
            fields=[
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('pincode', models.PositiveIntegerField()),
                ('locality', models.TextField()),
                ('address', models.TextField()),
                ('city_district_town', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=100)),
                ('customer_product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('Categorie', models.CharField(max_length=200)),
                ('cost', models.PositiveIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('agentorders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agents.agentorders')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='agentorders',
            name='agentsusers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agents.agentsusers'),
        ),
        migrations.CreateModel(
            name='AgentShopCategorie',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Agents.agentsusers')),
                ('agent_shop_categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NapsackAdmin.shopscategories')),
            ],
        ),
    ]
