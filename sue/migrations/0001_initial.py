# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentList',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('heading', models.CharField(help_text=b'The heading for the Document list', max_length=250)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='DocumentListItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('files', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='File', blank=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='DocumentListItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Document List Item Category',
                'verbose_name_plural': 'Document List Item Categories',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('logo', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Logo', blank=True)),
                ('quote', models.CharField(help_text=b'Quote text (optional)', max_length=2000, null=True, blank=True)),
                ('quote_author', models.CharField(help_text=b'Quote authors name', max_length=2000, null=True, blank=True)),
                ('quote_link', models.CharField(help_text=b"link to the author of the quote's site (optional)", max_length=2000, null=True, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='ItemPorter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Porter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('homepage', models.ForeignKey(related_name='porter', blank=True, to='sue.HomePage', null=True)),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('featured_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Featured Image', blank=True)),
                ('short_description', mezzanine.core.fields.RichTextField(blank=True)),
                ('href', models.CharField(help_text=b'A link to the finished project (optional)', max_length=2000, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio item',
                'verbose_name_plural': 'Portfolio items',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='PortfolioItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Portfolio Item Category',
                'verbose_name_plural': 'Portfolio Item Categories',
            },
        ),
        migrations.CreateModel(
            name='PortfolioItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('portfolioitem', models.ForeignKey(related_name='images', to='sue.PortfolioItem')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Portfolios',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolios',
                'verbose_name_plural': "Portfolios'",
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('featured_image', models.NullBooleanField(help_text=b'The active 1st image to appear')),
                ('main_label', models.CharField(max_length=2000, null=True, blank=True)),
                ('sub_label', models.CharField(max_length=2000, null=True, blank=True)),
                ('homepage', models.ForeignKey(related_name='slides', to='sue.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='TempPortfolio',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'TempPortfolio',
                'verbose_name_plural': 'TempPortfolios',
            },
            bases=('pages.page',),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='categories',
            field=models.ManyToManyField(related_name='portfolioitems', verbose_name='Categories', to='sue.PortfolioItemCategory', blank=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_item',
            field=models.ForeignKey(blank=True, to='sue.PortfolioItem', null=True),
        ),
        migrations.AddField(
            model_name='porter',
            name='multiport',
            field=models.ForeignKey(blank=True, to='sue.Portfolio', help_text=b'If selected items from this portfolio will be featured on the home page.', null=True),
        ),
        migrations.AddField(
            model_name='itemporter',
            name='portfolio_item',
            field=models.ForeignKey(blank=True, to='sue.PortfolioItem', help_text=b'If selected portfolio items will be featured on this porfolio', null=True),
        ),
        migrations.AddField(
            model_name='itemporter',
            name='temp_portfolio',
            field=models.ForeignKey(related_name='item_porter', blank=True, to='sue.TempPortfolio', null=True),
        ),
        migrations.AddField(
            model_name='documentlistitem',
            name='category',
            field=models.ForeignKey(related_name='category', blank=True, to='sue.DocumentListItemCategory', null=True),
        ),
        migrations.AddField(
            model_name='documentlistitem',
            name='documentlist',
            field=models.ForeignKey(related_name='documents', blank=True, to='sue.DocumentList', null=True),
        ),
    ]
