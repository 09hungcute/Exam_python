import tkinter as tk
from tkinter import messagebox
from database import db

def save_appointment():
    patient_id = entry_patient_id.get()
    doctor_id = entry_doctor_id.get()
    date = entry_date.get()
    reason = entry_reason.get()

    if not patient_id or not doctor_id or not date:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    db.appointments.insert_one({
        "patient_id": int(patient_id),
        "doctor_id": int(doctor_id),
        "appointment_date": date,
        "reason": reason,
        "status": "pending"
    })

    messagebox.showinfo("Thành công", "Cuộc hẹn đã được đặt!")
    window.destroy()

def open_add_appointment_window():
    global window, entry_patient_id, entry_doctor_id, entry_date, entry_reason
    window = tk.Toplevel()
    window.title("Đặt cuộc hẹn")

    tk.Label(window, text="Mã bệnh nhân:").pack()
    entry_patient_id = tk.Entry(window)
    entry_patient_id.pack()

    tk.Label(window, text="Mã bác sĩ:").pack()
    entry_doctor_id = tk.Entry(window)
    entry_doctor_id.pack()

    tk.Label(window, text="Ngày hẹn (YYYY-MM-DD HH:MM):").pack()
    entry_date = tk.Entry(window)
    entry_date.pack()

    tk.Label(window, text="Lý do:").pack()
    entry_reason = tk.Entry(window)
    entry_reason.pack()

    tk.Button(window, text="Lưu", command=save_appointment).pack()
