# Copyright (c) 2025, Dharmendra and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data
# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from test_app.test.report.sml_sales_analytics.sml_sales_analytics import Analytics
# from erpnext.selling.report.sales_analytics.sales_analytics import Analytics

def execute(filters=None):
	return Analytics(filters).run()