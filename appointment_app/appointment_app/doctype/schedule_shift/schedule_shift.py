# Copyright (c) 2024, OSama alyahyawy and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import format_time  
class ScheduleShift(Document):
    # Set the title to start_time - end_time
	def before_save(self) :
		self.title = format_time(self.start_time,"HH-mm") +" - "+ format_time(self.end_time,"HH-mm")
