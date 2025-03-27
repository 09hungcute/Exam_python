import tkinter as tk
from gui.add_patient import open_add_patient_window
from gui.add_doctor import open_add_doctor_window
from gui.add_appointment import open_add_appointment_window

try:
    from gui.report import open_report_window
    has_report = True
except ImportError:
    has_report = False

def main_window():
    root = tk.Tk()
    root.title("Hệ thống quản lý bệnh viện")
    root.geometry("400x300")
    
    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="🏥 Hệ thống quản lý bệnh viện", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(frame, text="➕ Thêm bệnh nhân", command=open_add_patient_window, width=20).pack(pady=5)
    tk.Button(frame, text="👨‍⚕️ Thêm bác sĩ", command=open_add_doctor_window, width=20).pack(pady=5)
    tk.Button(frame, text="📅 Thêm cuộc hẹn", command=open_add_appointment_window, width=20).pack(pady=5)

    if has_report:
        tk.Button(frame, text="📊 Xem báo cáo", command=open_report_window, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_window()
