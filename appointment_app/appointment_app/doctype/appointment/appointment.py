# Copyright (c) 2024, OSama alyahyawy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Appointment(Document):
	def after_insert(self):
		self.queue_number = self.add_to_appointment_queue()

		frappe.cache().set_value("queue_number", self.queue_number)		
		self.save(ignore_permissions=True)

		
  

	def add_to_appointment_queue(self):
		filters = {
				"date": self.date,
				"shift": self.shift,
				"clinic": self.clinic,
			}
		appointment_queue_exists = frappe.db.exists(
			"Appointment Queue",
			filters,
		)

		if appointment_queue_exists:
			q = frappe.get_doc("Appointment Queue", filters)
		else:
			q = frappe.new_doc("Appointment Queue")
			q.update(filters)
			q.save(ignore_permissions=True)

		q.append("queue", {"appointment": self.name, "status": "Pending"})
		q.save(ignore_permissions=True)	
		return len(q.queue)
 
 
 # def after_insert(self):
	# 	self.queue_number =  self.add_to_appointment_queue()
	
 
 
	# def add_to_appointment_queue(self):
	# 	filters = {
	# 		"date"	:self.date,
	# 		"clinic" :self.clinic,
	# 		"shift" :self.shift,
	# 	}
  
	# 	appointment_queue_exist = frappe.db.exists(
	# 		"Appointment Queue",
	# 		filters ,
	# 	)
  
	# 	if appointment_queue_exist :
	# 		q = frappe.get_doc('Appointment Queue', filters )
	# 	else :
	# 		q = frappe.new_doc('Appointment Queue')
	# 		q.date   = self.date
	# 		q.clinic = self.clinic		
	# 		q.shift   = self.shift
	# 		q.insert()
	# 		# q.update(filters)
	# 		# q.save(ignore_permissions = True )   

	# 	q.append("queue" , {"appointment":self.name ,"status":"Pending" })
	# 	q.save(ignore_permissions = True)
	# 	return len(q.queue)

    

