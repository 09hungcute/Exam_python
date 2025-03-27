import tkinter as tk
from tkinter import messagebox
from database import db, get_next_sequence

def open_add_doctor_window():
    def add_doctor():
        full_name = entry_name.get()
        specialization = entry_specialization.get()
        phone = entry_phone.get()
        email = entry_email.get()
        experience = entry_experience.get()

        if not (full_name and specialization):
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        doctor_id = get_next_sequence("doctors")  # Lấy ID tự động tăng

        db.doctors.insert_one({
            "doctor_id": doctor_id,
            "full_name": full_name,
            "specialization": specialization,
            "phone_number": phone,
            "email": email,
            "years_of_experience": int(experience)
        })

        messagebox.showinfo("Thành công", f"Thêm bác sĩ ID {doctor_id} thành công!")
        window.destroy()

    window = tk.Toplevel()
    window.title("Thêm Bác Sĩ")

    tk.Label(window, text="Họ tên:").pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    tk.Label(window, text="Chuyên môn:").pack()
    entry_specialization = tk.Entry(window)
    entry_specialization.pack()

    tk.Label(window, text="Số điện thoại:").pack()
    entry_phone = tk.Entry(window)
    entry_phone.pack()

    tk.Label(window, text="Email:").pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    tk.Label(window, text="Kinh nghiệm (số năm):").pack()
    entry_experience = tk.Entry(window)
    entry_experience.pack()

    tk.Button(window, text="Thêm", command=add_doctor).pack()

    window.mainloop()
