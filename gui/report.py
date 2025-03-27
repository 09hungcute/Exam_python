import tkinter as tk
from tkinter import ttk
from database import db

def open_report_window():
    window = tk.Toplevel()
    window.title("Báo Cáo Lịch Hẹn")
    window.geometry("600x400")

    # Tiêu đề bảng
    columns = ("Tên bệnh nhân", "Bác sĩ", "Ngày tháng", "Lý do")
    tree = ttk.Treeview(window, columns=columns, show="headings")

    # Định nghĩa cột
    tree.heading("Tên bệnh nhân", text="Tên bệnh nhân")
    tree.heading("Bác sĩ", text="Bác sĩ")
    tree.heading("Ngày tháng", text="Ngày tháng")
    tree.heading("Lý do", text="Lý do")

    tree.column("Tên bệnh nhân", width=150)
    tree.column("Bác sĩ", width=150)
    tree.column("Ngày tháng", width=150)
    tree.column("Lý do", width=150)

    # Lấy dữ liệu từ MongoDB
    appointments = db.appointments.find()
    
    for appointment in appointments:
        patient = db.patients.find_one({"patient_id": appointment["patient_id"]})
        doctor = db.doctors.find_one({"doctor_id": appointment["doctor_id"]})
        
        patient_name = patient["full_name"] if patient else "Unknown"
        doctor_name = doctor["full_name"] if doctor else "Unknown"
        appointment_date = appointment["appointment_date"]
        reason = appointment.get("reason", "Không có lý do")

        tree.insert("", "end", values=(patient_name, doctor_name, appointment_date, reason))

    tree.pack(expand=True, fill="both")

    window.mainloop()
