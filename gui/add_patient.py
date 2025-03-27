import tkinter as tk
from tkinter import messagebox
from database import db, get_next_sequence

def open_add_patient_window():
    def add_patient():
        full_name = entry_name.get()
        dob = entry_dob.get()
        gender = entry_gender.get()
        address = entry_address.get()
        phone = entry_phone.get()
        email = entry_email.get()

        if not (full_name and dob and gender):
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        patient_id = get_next_sequence("patients")  

        db.patients.insert_one({
            "patient_id": patient_id,
            "full_name": full_name,
            "date_of_birth": dob,
            "gender": gender,
            "address": address,
            "phone_number": phone,
            "email": email
        })

        messagebox.showinfo("Thành công", f"Thêm bệnh nhân ID {patient_id} thành công!")
        window.destroy()

    window = tk.Toplevel()
    window.title("Thêm Bệnh Nhân")

    tk.Label(window, text="Họ tên:").pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    tk.Label(window, text="Ngày sinh (YYYY-MM-DD):").pack()
    entry_dob = tk.Entry(window)
    entry_dob.pack()

    tk.Label(window, text="Giới tính:").pack()
    entry_gender = tk.Entry(window)
    entry_gender.pack()

    tk.Label(window, text="Địa chỉ:").pack()
    entry_address = tk.Entry(window)
    entry_address.pack()

    tk.Label(window, text="Số điện thoại:").pack()
    entry_phone = tk.Entry(window)
    entry_phone.pack()

    tk.Label(window, text="Email:").pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    tk.Button(window, text="Thêm", command=add_patient).pack()

    window.mainloop()
