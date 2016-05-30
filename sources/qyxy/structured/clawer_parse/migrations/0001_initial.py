# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('credit_code', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_name', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_type', models.CharField(max_length=100, null=True, blank=True)),
                ('corporation', models.CharField(max_length=30, null=True, blank=True)),
                ('register_capital', models.FloatField(null=True)),
                ('establish_date', models.DateField(null=True)),
                ('place', models.CharField(max_length=100, null=True, blank=True)),
                ('time_start', models.DateField(null=True)),
                ('time_end', models.DateField(null=True)),
                ('business_scope', models.TextField(null=True)),
                ('register_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('check_date', models.DateField(null=True)),
                ('register_status', models.CharField(max_length=50, null=True, blank=True)),
                ('register_num', models.CharField(max_length=50, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'basic',
            }, ),
        migrations.CreateModel(
            name='EnterAdministrativeLicense',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('license_num', models.CharField(max_length=100, null=True, blank=True)),
                ('license_filename', models.CharField(max_length=50, null=True, blank=True)),
                ('license_begin_date', models.DateField(null=True)),
                ('license_end_date', models.DateField(null=True)),
                ('license_authority', models.CharField(max_length=30, null=True, blank=True)),
                ('license_content', models.TextField(null=True, blank=True)),
                ('license_status', models.TextField(null=True, blank=True)),
                ('license_detail', models.TextField(null=True, blank=True)),
                ('license_register_time', models.DateField(null=True)),
                ('license_publicity_time', models.DateField(null=True)),
                ('license_change_item', models.CharField(max_length=20, null=True, blank=True)),
                ('license_change_time', models.DateField(null=True)),
                ('license_content_before', models.CharField(max_length=50, null=True,
                                                            blank=True)),
                ('license_content_after', models.CharField(max_length=50, null=True,
                                                           blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_administrative_license',
            }, ),
        migrations.CreateModel(
            name='EnterAdministrativePenalty',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('penalty_decision_num', models.CharField(max_length=30, null=True, blank=True)),
                ('illegal_type', models.CharField(max_length=100, null=True, blank=True)),
                ('administrative_penalty_content', models.CharField(max_length=30, null=True,
                                                                    blank=True)),
                ('decision_gov', models.CharField(max_length=30, null=True, blank=True)),
                ('decision_date', models.DateField(null=True)),
                ('penalty_comment', models.CharField(max_length=50, null=True, blank=True)),
                ('penalty_publicit_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_administrative_penalty',
            }, ),
        migrations.CreateModel(
            name='EnterAnnualReport',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('report_year', models.IntegerField(null=True)),
                ('publicity_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_annual_report',
            }, ),
        migrations.CreateModel(
            name='EnterIntellectualPropertyPledge',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('credit_code', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_name', models.CharField(max_length=50, null=True, blank=True)),
                ('property_type', models.CharField(max_length=30, null=True, blank=True)),
                ('pledgor_name', models.CharField(max_length=30, null=True, blank=True)),
                ('mortgagee_name', models.CharField(max_length=30, null=True, blank=True)),
                ('mortgage_register_date', models.DateField(null=True)),
                ('property_status', models.CharField(max_length=40, null=True, blank=True)),
                ('property_pledge_change', models.CharField(max_length=40, null=True,
                                                            blank=True)),
                ('property_pledge_register_gov', models.CharField(max_length=30, null=True,
                                                                  blank=True)),
                ('property_pledge_register_date', models.DateField(null=True)),
                ('property_pledge_publicity_time', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_intellectual_property_pledge',
            }, ),
        migrations.CreateModel(
            name='EnterModification',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('modify_item', models.TextField(null=True, blank=True)),
                ('modify_before', models.CharField(max_length=50, null=True, blank=True)),
                ('modify_after', models.CharField(max_length=50, null=True, blank=True)),
                ('modify_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_modification',
            }, ),
        migrations.CreateModel(
            name='EnterSharechange',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('shareholder', models.CharField(max_length=100, null=True, blank=True)),
                ('share_ratio_before', models.FloatField(null=True)),
                ('share_ratio_after', models.FloatField(null=True)),
                ('share_change_date', models.DateField(null=True)),
                ('sharechange_register_date', models.DateField(null=True)),
                ('sharechange_publicity_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_sharechange',
            }, ),
        migrations.CreateModel(
            name='EnterShareholder',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('shareholder_name', models.CharField(max_length=200, null=True, blank=True)),
                ('subscription_amount', models.FloatField(null=True)),
                ('paid_amount', models.FloatField(null=True)),
                ('subscription_type', models.CharField(max_length=100, null=True, blank=True)),
                ('subscription_date', models.DateField(null=True)),
                ('subscription_money_amount', models.FloatField(null=True)),
                ('paid_type', models.CharField(max_length=100, null=True, blank=True)),
                ('paid_money_amount', models.FloatField(null=True)),
                ('paid_date', models.DateField(null=True)),
                ('shareholder_type', models.CharField(max_length=20, null=True, blank=True)),
                ('subscription_publicity_time', models.DateField(null=True)),
                ('paid_publicity_time', models.DateField(null=True)),
                ('publicity_time', models.DateField(null=True)),
                ('modify_time', models.DateField(null=True)),
                ('detals', models.CharField(max_length=256, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'enter_shareholder',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceAdministrativePenalty',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('penalty_decision_num', models.CharField(max_length=30, null=True, blank=True)),
                ('illegal_type', models.CharField(max_length=100, null=True, blank=True)),
                ('penalty_content', models.CharField(max_length=50, null=True, blank=True)),
                ('penalty_decision_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('penalty_decision_date', models.DateField(null=True)),
                ('detail', models.TextField(null=True, blank=True)),
                ('penalty_register_date', models.DateField(null=True)),
                ('enter_name', models.CharField(max_length=50, null=True, blank=True)),
                ('creidit_code', models.CharField(max_length=20, null=True, blank=True)),
                ('corporation', models.CharField(max_length=30, null=True, blank=True)),
                ('penalty_publicity_time', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=30, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_administrative_penalty',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceBranch',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('enter_code', models.CharField(max_length=100, null=True, blank=True)),
                ('branch_name', models.CharField(max_length=100, null=True, blank=True)),
                ('register_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_branch',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceChange',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('modify_item', models.TextField(null=True, blank=True)),
                ('modify_before', models.TextField(null=True, blank=True)),
                ('modify_after', models.TextField(max_length=50, null=True, blank=True)),
                ('modify_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_change',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceCheck',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('check_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('check_type', models.CharField(max_length=20, null=True, blank=True)),
                ('check_date', models.DateField(null=True)),
                ('check_result', models.CharField(max_length=50, null=True, blank=True)),
                ('check_comment', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_check',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceClear',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('person_in_charge', models.CharField(max_length=30, null=True, blank=True)),
                ('persons', models.CharField(max_length=100, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_clear',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceDetailGuarantee',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('register_code', models.CharField(max_length=20, null=True, blank=True)),
                ('sharechange_register_date', models.DateField(null=True)),
                ('register_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('register_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_detail_guarantee',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceException',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('list_on_reason', models.CharField(max_length=100, null=True, blank=True)),
                ('list_on_date', models.DateField(null=True)),
                ('list_out_reason', models.CharField(max_length=100, null=True, blank=True)),
                ('list_out_date', models.DateField(null=True)),
                ('list_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('list_on_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('list_out_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_exception',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceIllegal',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('list_on_reason', models.CharField(max_length=100, null=True, blank=True)),
                ('list_on_date', models.DateField(null=True)),
                ('list_out_reason', models.CharField(max_length=100, null=True, blank=True)),
                ('list_out_date', models.DateField(max_length=100, null=True, blank=True)),
                ('decision_gov', models.CharField(max_length=30, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_illegal',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceMainperson',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('position', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_mainperson',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceMortgage',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('register_num', models.CharField(max_length=50, null=True, blank=True)),
                ('sharechange_register_date', models.DateField(null=True)),
                ('register_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('guarantee_debt_amount', models.FloatField(null=True)),
                ('status', models.CharField(max_length=20, null=True, blank=True)),
                ('publicity_time', models.DateField(null=True)),
                ('details', models.TextField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_mortgage',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceMortgageDetailChange',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('modify_date', models.DateField(null=True)),
                ('modify_content', models.TextField(null=True)),
                ('register_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_mortgage_detail_change',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceMortgageDetailGuarantee',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('check_type', models.CharField(max_length=20, null=True, blank=True)),
                ('amount', models.FloatField(null=True)),
                ('guarantee_scope', models.CharField(max_length=100, null=True, blank=True)),
                ('debtor_duration', models.CharField(max_length=20, null=True, blank=True)),
                ('comment', models.CharField(max_length=100, null=True, blank=True)),
                ('register_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_cortgage_detail_guarantee',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceMortgageGuaranty',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('ownership', models.CharField(max_length=30, null=True, blank=True)),
                ('details', models.TextField(null=True)),
                ('coments', models.CharField(max_length=100, null=True, blank=True)),
                ('register_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_mortgage_guaranty',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceRevoke',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('revoke_item', models.CharField(max_length=30, null=True, blank=True)),
                ('content_before_revoke', models.CharField(max_length=50, null=True,
                                                           blank=True)),
                ('content_after_revoke', models.CharField(max_length=50, null=True, blank=True)),
                ('revoke_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_revoke',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceShareholders',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('shareholder_type', models.CharField(max_length=100, null=True, blank=True)),
                ('shareholder_name', models.CharField(max_length=200, null=True, blank=True)),
                ('certificate_type', models.CharField(max_length=100, null=True, blank=True)),
                ('certificate_number', models.CharField(max_length=100, null=True, blank=True)),
                ('subscription_amount', models.FloatField(null=True)),
                ('paid_amount', models.FloatField(null=True)),
                ('subscription_type', models.CharField(max_length=100, null=True, blank=True)),
                ('subscription_date', models.DateField(null=True)),
                ('subscription_money_amount', models.FloatField(null=True)),
                ('paid_type', models.CharField(max_length=100, null=True, blank=True)),
                ('paid_money_amount', models.FloatField(null=True)),
                ('paid_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_shareholders',
            }, ),
        migrations.CreateModel(
            name='IndustryCommerceSharepledge',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('register_num', models.CharField(max_length=50, null=True, blank=True)),
                ('pledgor', models.CharField(max_length=30, null=True, blank=True)),
                ('pledgor_certificate_code', models.CharField(max_length=20, null=True,
                                                              blank=True)),
                ('share_pledge_num', models.FloatField(null=True)),
                ('mortgagee', models.CharField(max_length=30, null=True, blank=True)),
                ('mortgagee_certificate_code', models.CharField(max_length=20, null=True,
                                                                blank=True)),
                ('sharechange_register_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=20, null=True, blank=True)),
                ('change_detail', models.CharField(max_length=100, null=True, blank=True)),
                ('publicity_time', models.DateField(null=True)),
                ('modify_date', models.DateField(null=True)),
                ('modify_content', models.TextField(null=True)),
                ('register_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_commerce_sharepledge',
            }, ),
        migrations.CreateModel(
            name='IndustryMortgageDetailMortgagee',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('mortgagee_name', models.CharField(max_length=30, null=True, blank=True)),
                ('mortgagee_certificate_type', models.CharField(max_length=20, null=True,
                                                                blank=True)),
                ('pledgor_certificate_code', models.CharField(max_length=20, null=True,
                                                              blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'industry_mortgage_detail_mortgagee',
            }, ),
        migrations.CreateModel(
            name='JudicialShareFreeze',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('been_excute_person', models.CharField(max_length=30, null=True, blank=True)),
                ('share_num', models.IntegerField(null=True)),
                ('excute_court', models.CharField(max_length=30, null=True, blank=True)),
                ('notice_num', models.CharField(max_length=30, null=True, blank=True)),
                ('freeze_status', models.CharField(max_length=30, null=True, blank=True)),
                ('freeze_detail', models.TextField(null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'judicial_share_freeze',
            }, ),
        migrations.CreateModel(
            name='JudicialShareholderChange',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('been_excute_name', models.CharField(max_length=30, null=True, blank=True)),
                ('share_num', models.IntegerField(null=True)),
                ('excute_court', models.CharField(max_length=30, null=True, blank=True)),
                ('assignee', models.CharField(max_length=30, null=True, blank=True)),
                ('detail', models.TextField(null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'judicial_shareholder_change',
            }, ),
        migrations.CreateModel(
            name='OtherAdministrativeChange',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('administrative_change_item', models.CharField(max_length=30, null=True,
                                                                blank=True)),
                ('administrative_change_tme', models.DateField(null=True)),
                ('administrative_change_before', models.CharField(max_length=50, null=True,
                                                                  blank=True)),
                ('administrative_change_after', models.CharField(max_length=50, null=True,
                                                                 blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'other_administrative_change',
            }, ),
        migrations.CreateModel(
            name='OtherAdministrativeLicense',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('license_file_num', models.CharField(max_length=30, null=True, blank=True)),
                ('license_filename', models.CharField(max_length=50, null=True, blank=True)),
                ('license_begin_date', models.DateField(null=True)),
                ('license_end_date', models.DateField(null=True)),
                ('license_content', models.TextField(null=True, blank=True)),
                ('license_authority_gov', models.CharField(max_length=50, null=True,
                                                           blank=True)),
                ('license_status', models.TextField(null=True, blank=True)),
                ('license_detail', models.TextField(null=True, blank=True)),
                ('license_valid_date', models.DateField(null=True)),
                ('source', models.CharField(max_length=10, null=True, blank=True)),
                ('update_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'other_administrative_license',
            }, ),
        migrations.CreateModel(
            name='OtherAdministrativePenalty',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('penalty_decision_num', models.IntegerField(null=True)),
                ('illegal_type', models.CharField(max_length=100, null=True, blank=True)),
                ('penalty_content', models.CharField(max_length=50, null=True, blank=True)),
                ('penalty_decision_gov', models.CharField(max_length=50, null=True, blank=True)),
                ('penalty_decision_date', models.DateField(null=True)),
                ('detail', models.TextField(null=True, blank=True)),
                ('penalty_type', models.CharField(max_length=30, null=True, blank=True)),
                ('forfeiture_money', models.FloatField(null=True)),
                ('confiscate_money', models.FloatField(null=True)),
                ('source', models.CharField(max_length=20, null=True, blank=True)),
                ('update_date', models.DateField(null=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'other_administrative_penalty',
            }, ),
        migrations.CreateModel(
            name='OtherProductionSecurity',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('accidient_number', models.IntegerField(null=True)),
                ('accident_level', models.IntegerField(null=True)),
                ('accidient_type', models.CharField(max_length=30, null=True, blank=True)),
                ('accidient_time', models.DateField(null=True)),
                ('death_num', models.IntegerField(null=True)),
                ('info_publish_gov', models.CharField(max_length=30, null=True, blank=True)),
                ('enter_id', models.CharField(max_length=20, null=True, blank=True)),
                ('bas_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'other_production_security',
            }, ),
        migrations.CreateModel(
            name='YearReportAssets',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('asset_all', models.FloatField(null=True)),
                ('owner_asset', models.FloatField(null=True)),
                ('business_income', models.FloatField(null=True)),
                ('profit', models.FloatField(null=True)),
                ('main_business_income', models.FloatField(null=True)),
                ('net_income', models.FloatField(null=True)),
                ('tax', models.FloatField(null=True)),
                ('debts', models.FloatField(null=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_assets',
            }, ),
        migrations.CreateModel(
            name='YearReportBasic',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('credit_code', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_name', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=30, null=True, blank=True)),
                ('enter_place', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('shareholder_change', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20, null=True, blank=True)),
                ('web_onlinestore', models.BooleanField(default=False)),
                ('staff_number', models.IntegerField(null=True)),
                ('register_num', models.CharField(max_length=50, null=True, blank=True)),
                ('is_warrandice', models.CharField(max_length=10, null=True, blank=True)),
                ('is_invest', models.BooleanField(default=False)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_basic',
            }, ),
        migrations.CreateModel(
            name='YearReportCorrect',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('correct_item', models.CharField(max_length=30, null=True, blank=True)),
                ('correct_reason', models.CharField(max_length=50, null=True, blank=True)),
                ('correct_time', models.DateField(null=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_correct',
            }, ),
        migrations.CreateModel(
            name='YearReportInvestment',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('invest_enter_name', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_code', models.CharField(max_length=100, null=True, blank=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_investment',
            }, ),
        migrations.CreateModel(
            name='YearReportModification',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('modify_item', models.TextField(null=True, blank=True)),
                ('modify_before', models.TextField(max_length=50, null=True, blank=True)),
                ('modify_after', models.TextField(max_length=50, null=True, blank=True)),
                ('modify_date', models.DateField(null=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_modification',
            }, ),
        migrations.CreateModel(
            name='YearReportOnline',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('online_type', models.CharField(max_length=100, null=True, blank=True)),
                ('enter_name', models.CharField(max_length=50, null=True, blank=True)),
                ('enter_url', models.TextField(null=True, blank=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_online',
            }, ),
        migrations.CreateModel(
            name='YearReportSharechange',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('shareholder', models.CharField(max_length=100, null=True, blank=True)),
                ('shares_before', models.FloatField(null=True)),
                ('shares_after', models.FloatField(null=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_sharechange',
            }, ),
        migrations.CreateModel(
            name='YearReportShareholder',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('shareholder', models.CharField(max_length=100, null=True, blank=True)),
                ('subscription_money_amount', models.FloatField(null=True)),
                ('subscription_time', models.DateField(null=True)),
                ('subscription_type', models.CharField(max_length=100, null=True, blank=True)),
                ('paid_money_amount', models.FloatField(null=True)),
                ('paid_time', models.DateField(null=True)),
                ('paid_type', models.CharField(max_length=100, null=True, blank=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_shareholder',
            }, ),
        migrations.CreateModel(
            name='YearReportWarrandice',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False,
                    auto_created=True, primary_key=True)),
                ('creditor', models.CharField(max_length=200, null=True, blank=True)),
                ('debtor', models.CharField(max_length=30, null=True, blank=True)),
                ('main_creditor_right', models.CharField(max_length=30, null=True, blank=True)),
                ('main_creditor_right_amount', models.FloatField(null=True)),
                ('fullfill_debt_duration', models.CharField(max_length=100, null=True,
                                                            blank=True)),
                ('guarantee_duration', models.CharField(max_length=30, null=True, blank=True)),
                ('guarantee_type', models.CharField(max_length=30, null=True, blank=True)),
                ('warrandice_scope', models.CharField(max_length=100, null=True, blank=True)),
                ('year_report_id', models.CharField(max_length=20, null=True, blank=True)),
                ('enter_id', models.IntegerField(null=True)),
                ('version', models.IntegerField(default=1)),
                ('invalidation', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'year_report_warrandice',
            }, ),
    ]
