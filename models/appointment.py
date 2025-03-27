from datetime import datetime

class Appointment:
    def __init__(self, patient_id, doctor_id, appointment_date, reason, status="Pending"):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
        self.reason = reason
        self.status = status

    def to_dict(self):
        return self.__dict__
