from tkinter import *
from PIL import Image, ImageTk
from  tkinter import ttk
import random
from time import strftime
from datetime import datetime
import sqlite3
from tkinter import messagebox
class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng khách sạn")
        self.root.geometry("1050x600+230+125")

        self.var_id = StringVar()
        self.var_employ_name = StringVar()
        self.var_mobile = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_user = StringVar()
        self.var_pass = StringVar()
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Nhân viên",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=10, width=410, height=480)
        lbl_cust_ref = Label(labelframeleft, text="ID :", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_id, font=("Arial", 13, "bold"), width=20, )
        enty_ref.grid(row=0, column=1)

        lbl_cust_ref = Label(labelframeleft, text="Họ tên :", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=1, column=0, sticky=W)
        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_employ_name, font=("Arial", 13, "bold"), width=20,)
        enty_ref.grid(row=1, column=1)

        cname = Label(labelframeleft, font=("Arial", 12, "bold"), text="Số điện thoại", padx=2, pady=6)
        cname.grid(row=2, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_mobile, font=("Arial", 13, "bold"), width=20)
        txtcname.grid(row=2, column=1)
        label_gender = Label(labelframeleft, font=("Arial", 12, "bold"), text="Giới tính:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gerder = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 12, "bold"), width=18,
                                    state="readonly")
        combo_gerder["value"] = ("Nam", "Nữ", "Khác")
        combo_gerder.current(0)
        combo_gerder.grid(row=3, column=1)

        lblEmail = Label(labelframeleft, font=("Arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=4, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("Arial", 13, "bold"), width=20)
        txtEmail.grid(row=4, column=1)

        cname = Label(labelframeleft, font=("Arial", 12, "bold"), text="Tài khoản:", padx=2, pady=6)
        cname.grid(row=5, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_user, font=("Arial", 13, "bold"), width=20)
        txtcname.grid(row=5, column=1)

        cname = Label(labelframeleft, font=("Arial", 12, "bold"), text="Mật khẩu:", padx=2, pady=6)
        cname.grid(row=6, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_pass, font=("Arial", 13, "bold"), width=20)
        txtcname.grid(row=6, column=1)

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Thêm", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Sửa", command=self.update, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Xóa", command=self.mDelete, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Làm mới", command=self.reset, font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Xem nhân viên và tìm kiếm",
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=420, y=10, width=620, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Tìm kiếm:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.serch_var, font=("arial", 12, "bold"), width=6,
                                    state="readonly")
        combo_Search["value"] = ("ID")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_serch = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_serch, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Tìm kiếm", command=self.search, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Hiển thị tất cả", command=self.fetch_data, font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=620, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,
                                               columns=("id", "ho_ten", "so_dien_thoai","gioi_tinh", "email", "tai_khoan", "mat_khau"),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("id", text="ID")
        self.Cust_Details_Table.heading("ho_ten", text="Họ Tên")
        self.Cust_Details_Table.heading("so_dien_thoai", text="Số điện thoại")
        self.Cust_Details_Table.heading("gioi_tinh", text="Giới tính")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("tai_khoan", text="Tài khoản")
        self.Cust_Details_Table.heading("mat_khau", text="Mật khẩu")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("id", width=100)
        self.Cust_Details_Table.column("ho_ten", width=100)
        self.Cust_Details_Table.column("so_dien_thoai", width=100)
        self.Cust_Details_Table.column("gioi_tinh", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("tai_khoan", width=100)
        self.Cust_Details_Table.column("mat_khau", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_employ_name.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin !", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO nhanvien (id,ho_ten, so_dien_thoai, gioi_tinh,email, tai_khoan, mat_khau)
                    VALUES (?, ?, ?, ?, ?, ?,?)
                """, (
                    self.var_id.get(),
                    self.var_employ_name.get(),
                    self.var_mobile.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_user.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Thêm nhân viên thành công ", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

            finally:
                if conn:
                    conn.close()

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    UPDATE nhanvien
                    SET ho_ten=?, so_dien_thoai=?, gioi_tinh=?,email=?, tai_khoan=?, mat_khau=?
                    WHERE id=?
                """, (
                    self.var_employ_name.get(),
                    self.var_mobile.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_user.get(),
                    self.var_pass.get(),
                    self.var_id.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Cập nhật nhân viên thành công ", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Bạn có chắc muôn xóa nhân viên này ?",
                                      parent=self.root)

        if mDelete:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()
                query = "DELETE FROM nhanvien WHERE id=?"
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                messagebox.showinfo("Success", "Đã xóa nhân viên thành công", parent=self.root)
                self.fetch_data()

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()
        else:
            return

    def reset(self):
        self.var_id.set("")
        self.var_employ_name.set("")
        self.var_mobile.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_user.set("")
        self.var_pass.set("")

    def search(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()
            search_column = self.serch_var.get()
            search_value = self.txt_serch.get()

            query = f"SELECT * FROM nhanvien WHERE {search_column} LIKE ?"
            my_cursor.execute(query, (f"%{search_value}%",))
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
            else:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

        finally:
            if conn:
                conn.close()

    def fetch_data(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM nhanvien")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)

        except Exception as e:
            print(f"Lỗi khi truy vấn dữ liệu: {e}")

        finally:
            if conn:
                conn.close()

    def get_cuersor(self, event=""):
        cusrsor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cusrsor_row)
        row = content["values"]

        self.var_id.set(row[0])
        self.var_employ_name.set(row[1])
        self.var_mobile.set(row[2])
        self.var_gender.set(row[3])
        self.var_email.set(row[4])
        self.var_user.set(row[5])
        self.var_pass.set(row[6])
if __name__ == "__main__":
        root = Tk()
        obj = Employee(root)
        root.mainloop()
