from tkinter import *
from PIL import Image, ImageTk
from  tkinter import ttk
import random
import sqlite3
from tkinter import messagebox
class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng khách sạn")
        self.root.geometry("1050x600+230+125")

        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_adderss = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Khách hàng",font=("times new roman", 12, "bold"),padx =2)
        labelframeleft.place(x=5, y=10, width=410, height=480)

        lbl_cust_ref = Label(labelframeleft, text="Mã khách hàng", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref, font=("Arial", 13, "bold"), width=20,state="readonly")
        enty_ref.grid(row=0, column=1)

        cname = Label(labelframeleft, font=("Arial", 12, "bold"), text="Tên :", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, font=("Arial", 13, "bold"), width=20)
        txtcname.grid(row=1, column=1)

        lblmname = Label(labelframeleft, font=("Arial", 12, "bold"), text="Họ :", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_mother, font=("Arial", 13, "bold"), width=20)
        txtmname.grid(row=2, column=1)

        label_gender = Label(labelframeleft, font=("Arial", 12, "bold"), text="Giới tính:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gerder =ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12 ,"bold"),width = 18,state="readonly")
        combo_gerder["value"] = ("Nam","Nữ","Khác")
        combo_gerder.current(0)
        combo_gerder.grid(row =3,column =1)

        lblPostCode = Label(labelframeleft, font=("Arial", 12, "bold"), text="Mã bưu điện:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_post, font=("Arial", 13, "bold"), width=20)
        txtPostCode.grid(row=4, column=1)

        lblMobile = Label(labelframeleft, font=("Arial", 12, "bold"), text="Số điện thoại", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, font=("Arial", 13, "bold"), width=20)
        txtMobile.grid(row=5, column=1)

        lblEmail = Label(labelframeleft, font=("Arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, font=("Arial", 13, "bold"), width=20)
        txtEmail.grid(row=6, column=1)

        lblNationality = Label(labelframeleft, font=("Arial", 12, "bold"), text="Quốc tịch:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("Arial", 12, "bold"), width=18, state="readonly")
        combo_Nationality["values"] = ("Việt Nam", "Mỹ", "Trung Quốc")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)
        lblIdProof = Label(labelframeleft, font=("Arial", 12, "bold"), text="Loại bằng chứng ID:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("Arial", 12, "bold"), width=18, state="readonly")
        combo_id["values"] = ("CCCD", "CMND","Bằng lái xe")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        lblIdNumber = Label(labelframeleft, font=("Arial", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=("Arial", 13, "bold"), width=20)
        txtIdNumber.grid(row=9, column=1)

        lblAddress = Label(labelframeleft, font=("Arial", 12, "bold"), text="Địa chỉ", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_adderss, font=("Arial", 13, "bold"), width=20)
        txtAddress.grid(row=10, column=1)



        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Thêm",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Sửa",command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Xóa", command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Làm mới",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)


        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Xem khách hàng và tìm kiếm",
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=420, y=10, width=620, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Tìm kiếm:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var =StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.serch_var, font=("arial", 12, "bold"), width=6, state="readonly")
        combo_Search["value"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_serch = StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_serch, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Tìm kiếm",command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Hiển thị tất cả",command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=620, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,
                                               columns=("ref", "name", "mother", "gender", "post", "mobile",
                                                        "email", "nationality", "idproof", "idnumber", "address"),
                                               xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Mã khách hàng")
        self.Cust_Details_Table.heading("name", text="Tên")
        self.Cust_Details_Table.heading("mother", text="Họ")
        self.Cust_Details_Table.heading("gender", text="Giới tính")
        self.Cust_Details_Table.heading("post", text="Mã bưu điện")
        self.Cust_Details_Table.heading("mobile", text="Số điện thoại")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Quốc tịch")
        self.Cust_Details_Table.heading("idproof", text="Loại bằng chứng ID")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Địa chỉ")
        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin !", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                my_cursor.execute("""
                    INSERT INTO customer (Ref,Name, Mother, Gender, PostCode, Mobile, Email, Nationality, Idproof, Idnumber, Address)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_adderss.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Đã thêm khách hàng thành công", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

            finally:
                if conn:
                    conn.close()
    def fetch_data(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM customer")
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

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_adderss.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                my_cursor.execute("""
                    UPDATE customer
                    SET Name=?, Mother=?, Gender=?, PostCode=?, Mobile=?, Email=?, Nationality=?, Idproof=?, Idnumber=?, Address=?
                    WHERE Mobile=?
                """, (
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_adderss.get(),
                    self.var_mobile.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Khách hàng đã được cập nhập thành công !", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()

    def mDelete(self):
        mDelete = messagebox.askyesno("Hệ thống quản lý phòng khách sạn", "Bạn có chắc muốn xóa khách hàng này ?",parent=self.root)

        if mDelete:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                query = "DELETE FROM customer WHERE Ref=?"
                value = (self.var_ref.get(),)
                my_cursor.execute(query, value)

                conn.commit()

                messagebox.showinfo("Success", "Xóa khách hàng thành công", parent=self.root)

                self.fetch_data()

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()
        else:
            return

    def reset(self):
        # self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
        # self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        # self.var_nationality.set("")
        # self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_adderss.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()

            search_column = self.serch_var.get()
            search_value = self.txt_serch.get()

            query = f"SELECT * FROM customer WHERE {search_column} LIKE ?"
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

if __name__ == "__main__":
        root = Tk()
        obj = Cust_Win(root)
        root.mainloop()
