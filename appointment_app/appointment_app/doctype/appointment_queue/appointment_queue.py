# Copyright (c) 2024, OSama alyahyawy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AppointmentQueue(Document):
    pass 
    
  
  
  
  
  
  
  
  
  
  
def create_queues_for_today():
	if frappe.flags.in_test:
		clinics = frappe.get_all("Clinic", filters={"is_published": True, "name": "Test Clinic"}, pluck="name")
	else:
		clinics = frappe.get_all("Clinic", filters={"is_published": True}, pluck="name")

	for clinic in clinics:
		# create an appointment queue if doesn't exists, use ignore_if_duplicate=True
		# to ignore duplicate entry error
		shifts = frappe.get_all("Schedule Shift", filters={"clinic": clinic}, pluck="name")
		for shift in shifts:
			frappe.get_doc(
				{
					"doctype": "Appointment Queue",
					"clinic": clinic,
					"date": frappe.utils.today(),
					"shift": shift,
				}
			).insert(ignore_if_duplicate=True)
     
    
# def create_queues_for_today(self):
#     # get all the clinics and for each clinic get the name with filter to the record that it's is_published is true
# 	clinics = frappe.get_all("Clinic", fields=["name"], filters={"is_published": True}) 
#     for clinic in clinics:
# 		#get all the shifts for the clinic
# 		shifts = frappe.get_all("Shift", fields=["name"], filters={"clinic": clinic.name})
# 		for shift in shifts:
# 			#make an appointment queue for each shift with the clinic , shift and date of today 
# 			#using frappe.get_doc 
# 			appointment_queue = frappe.get_doc({
# 				"doctype": "Appointment Queue",
# 				"clinic": clinic.name,
# 				"shift": shift.name,
# 				"date": frappe.utils.today()
# 			}).insert( ignore_if_duplicate = True )	
   
	
   