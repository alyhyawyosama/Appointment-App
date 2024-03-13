
import frappe

def get_context(context):
    context.no_cache = 1
    # Get the queue number that exist in frappe cache
    context.queue_number = frappe.cache().get_value("queue_number")
    #Delete the queue number from the cache
    frappe.cache().delete_value("queue_number")
        