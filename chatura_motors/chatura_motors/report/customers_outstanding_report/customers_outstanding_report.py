import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    """Defines the columns to display in the report."""
    return [
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 200},
        {"label": _("Total Outstanding"), "fieldname": "total_outstanding", "fieldtype": "Currency", "width": 150},
        {"label": _("Invoice Number"), "fieldname": "invoice_number", "fieldtype": "Link", "options": "Sales Invoice", "width": 150},
        {"label": _("Mobile Number"), "fieldname": "mobile_number", "fieldtype": "Data", "width": 150},
    ]

def get_data(filters):
    """Fetches the customer data with outstanding balances."""
    query = """
        SELECT
            c.customer_name,
            si.outstanding_amount AS total_outstanding,
            si.name AS invoice_number,
            c.mobile_no AS mobile_number
        FROM
            `tabSales Invoice` si
        JOIN
            `tabCustomer` c ON si.customer = c.name
        WHERE
            si.docstatus = 1
            AND si.outstanding_amount > 0
    """
    return frappe.db.sql(query, as_dict=True)
