from flask import Blueprint, request, json
from datetime import date
from backend.sqlconnection import SQL


class HelpFullFunc:
    def check_patient_info(patient_info: dict):
        
        full_name = patient_info.get("name")
        last_name = full_name.get("last_name")
        first_name = full_name.get("first_name")
        middle_name = full_name.get("middle_name")
        suffix = full_name.get("suffix")
        
        birthdate = patient_info.get("birth_date")
        month = birthdate.get("month")
        day = birthdate.get("day")
        year = birthdate.get("year")
        fulldate = date(year, month, day)
        
        gender = patient_info.get("gender")
        religion = patient_info.get("religion")
        nationality = patient_info.get("nationality")
        address = patient_info.get("address")
        
        contact = patient_info.get("contact")
        email = contact.get("email")
        mobile_number = contact.get("mobile_number")
        home_number = contact.get("home_number")
        office_number = contact.get("office_number")
        fax_number = contact.get("fax_number")
        
        if patient_info.get("is_minor"):
            guardian = patient_info.get("guardian")
            
            last_name = guardian.get("last_name")
            first_name = guardian.get("first_name")
            middle_name = guardian.get("middle_name")
            relationship = guardian.get("relationship")
            
        
            
        
            
        
        
        

class FormSubmission:
    def __init__(self):
        self.app = Blueprint("FormSubmission", __name__, url_prefix="/formSubmit")
        
    def routes(self):
        @self.app.route("/submit")
        def submit():
            data = request.json()
            
            patient_info = data.get("patientInfo")
            dental_history = data.get("dental_history")
            medical_history = data.get("medical_history")
            health_assessment = data.get("health_assessment")
            allergies = data.get("allergies")
            medical_conditions = data.get("medical_conditions")
            electronic_signature = data.get("electronic_signature")
            
    
    
      
            
    
            
            