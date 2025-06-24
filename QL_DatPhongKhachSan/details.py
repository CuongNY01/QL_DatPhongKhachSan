from tkinter import *
from PIL import Image, ImageTk
from  tkinter import ttk
import random
from time import strftime
from datetime import datetime
import sqlite3
from tkinter import messagebox
class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng khách sạn")
        self.root.geometry("1050x600+230+125")
        img3 = Image.open(r"hotel4.jpg")
        img3 = img3.resize((1050, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=10, y=10, width=1050, height=200)

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Thêm phòng mới",
                                    font=("times new roman", 11, "bold"), padx=2)
        labelframeleft.place(x=5, y=220, width=410, height=280)  # Điều chỉnh vị trí phù hợp
        # Customer Contact
        lbl_floor = Label(labelframeleft, text="ID ", font=("Arial", 11, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W,padx=20)
        self.var_floor =StringVar()
        enty_contact = ttk.Entry(labelframeleft,textvariable=self.var_floor, font=("Arial", 13, "bold"), width=13)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(labelframeleft, text="Số phòng", font=("arial", 11, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)
        self.var_roomNo = StringVar()
        enty_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomNo, font=("arial", 13, "bold"), width=13)
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Loại phòng", font=("arial", 11, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W, padx=20)
        self.var_RoomType = StringVar()
        enty_RoomType = ttk.Entry(labelframeleft,textvariable=self.var_RoomType, font=("arial", 13, "bold"), width=13)
        enty_RoomType.grid(row=2, column=1, sticky=W)

        lbl_RoomClass = Label(labelframeleft, text="Hạng phòng", font=("arial", 11, "bold"), padx=2, pady=6)
        lbl_RoomClass.grid(row=3, column=0, sticky=W, padx=20)
        self.var_RoomClass= StringVar()
        enty_RoomClass = ttk.Entry(labelframeleft, textvariable=self.var_RoomClass, font=("arial", 13, "bold"), width=13)
        enty_RoomClass.grid(row=3, column=1, sticky=W)
        # ====================== btns ======================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=150, width=412, height=40)

        btnAdd = Button(btn_frame, text="Thêm",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Sửa",command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold",
                           width=10)  # Fixed typo: btnUpadate -> btnUpdate
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Xóa",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Làm mới",command=self.reset_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Xem thông tin phòng",
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=420, y=220, width=620, height=280)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Tìm kiếm:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.serch_var, font=("arial", 12, "bold"), width=6,
                                    state="readonly")
        combo_Search["value"] = ("Floor")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_serch = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_serch, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Tìm kiếm",command=self.search, font=("arial", 11, "bold"), bg="black",
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
                                               columns=("floor", "roomno", "roomType","roomclass"),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("floor", text="ID")
        self.Cust_Details_Table.heading("roomno", text="Số phòng")
        self.Cust_Details_Table.heading("roomType", text="Loại phòng")
        self.Cust_Details_Table.heading("roomclass", text="Hạng phòng")
        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("floor", width=100)
        self.Cust_Details_Table.column("roomno", width=100)
        self.Cust_Details_Table.column("roomType", width=100)
        self.Cust_Details_Table.column("roomclass", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()

    def fetch_data(self):
        try:
            # Kết nối đến cơ sở dữ liệu SQLite3
            conn = sqlite3.connect("quanlyphongkhachsan.db")  # Tên file cơ sở dữ liệu SQLite3
            my_cursor = conn.cursor()

            # Thực thi truy vấn SELECT
            my_cursor.execute("SELECT * FROM details")
            rows = my_cursor.fetchall()

            # Kiểm tra xem có dữ liệu trả về không
            if len(rows) != 0:
                # Xóa dữ liệu cũ trong bảng (nếu có)
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

                # Thêm dữ liệu mới vào bảng
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)

        except Exception as e:
            # Thông báo lỗi nếu có vấn đề
            print(f"Lỗi khi truy vấn dữ liệu: {e}")

        finally:
            # Đóng kết nối
            if conn:
                conn.close()

    def get_cuersor(self, event=""):
        cusrsor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cusrsor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])
        self.var_RoomClass.set(row[3])
    def add_data(self):
        if self.var_roomNo.get() == "" or self.var_floor.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Kết nối đến cơ sở dữ liệu SQLite
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                # Thực thi truy vấn INSERT
                my_cursor.execute(
                    "INSERT INTO details (Floor, RoomNo,RoomType,RoomClass) VALUES (?, ?, ?,?)",
                    (
                        self.var_floor.get(),
                        self.var_roomNo.get(),
                        self.var_RoomType.get(),
                        self.var_RoomClass.get()

                    ))

                # Lưu thay đổi và đóng kết nối
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Thêm phòng thành công", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                # Kết nối đến cơ sở dữ liệu SQLite3
                conn = sqlite3.connect("quanlyphongkhachsan.db")  # Tên file cơ sở dữ liệu SQLite3
                my_cursor = conn.cursor()
                # Thực thi truy vấn UPDATE
                my_cursor.execute("""
                       UPDATE details 
                       SET Floor= ?,RoomType= ?, RoomClass = ? WHERE RoomNo= ? """,
                    (
                    self.var_floor.get(),
                    self.var_RoomType.get(),
                    self.var_RoomClass.get(),
                    self.var_roomNo.get()
                    # Điều kiện WHERE
                ))
                # Lưu thay đổi vào cơ sở dữ liệu
                conn.commit()
                self.fetch_data()
                conn.close()
                # Thông báo thành công
                messagebox.showinfo("Success", "Cập nhật phòng thành công ", parent=self.root)

            except Exception as e:
                # Thông báo lỗi nếu có vấn đề
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                # Đóng kết nối
                if conn:
                    conn.close()

    def mDelete(self):
        # Hiển thị hộp thoại xác nhận xóa
        mDelete = messagebox.askyesno("Hotel Management System", "Bạn có chắc muốn xóa phòng này ?",
                                      parent=self.root)

        if mDelete:  # Nếu người dùng chọn "Yes"
            try:
                # Kết nối đến cơ sở dữ liệu SQLite3
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                # Thực thi truy vấn DELETE
                query = "DELETE FROM details WHERE RoomNo=?"
                value = (self.var_roomNo.get(),)
                my_cursor.execute(query, value)

                # Lưu thay đổi vào cơ sở dữ liệu
                conn.commit()

                # Thông báo thành công
                messagebox.showinfo("Success", "Room deleted successfully", parent=self.root)
                self.fetch_data()

            except Exception as e:
                # Thông báo lỗi nếu có vấn đề
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                # Đóng kết nối
                if conn:
                    conn.close()
        else:
            # Nếu người dùng chọn "No", không làm gì cả
            return
    def search(self):
        try:
            # Kết nối đến cơ sở dữ liệu SQLite3
            conn = sqlite3.connect("quanlyphongkhachsan.db")  # Tên file cơ sở dữ liệu SQLite3
            my_cursor = conn.cursor()

            # Xây dựng truy vấn tìm kiếm
            search_column = self.serch_var.get()  # Cột cần tìm kiếm (ví dụ: Name, Mobile, Email, ...)
            search_value = self.txt_serch.get()  # Giá trị cần tìm kiếm

            # Thực thi truy vấn SELECT với điều kiện LIKE
            query = f"SELECT * FROM details WHERE {search_column} LIKE ?"
            my_cursor.execute(query, (f"%{search_value}%",))  # Sử dụng % để tìm kiếm phần tử chứa giá trị

            # Lấy kết quả từ truy vấn
            rows = my_cursor.fetchall()

            # Kiểm tra xem có dữ liệu trả về không
            if len(rows) != 0:
                # Xóa dữ liệu cũ trong bảng (nếu có)
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

                # Thêm dữ liệu mới vào bảng
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
            else:
                # Thông báo nếu không tìm thấy kết quả
                messagebox.showinfo("Info", "No matching records found", parent=self.root)

        except Exception as e:
            # Thông báo lỗi nếu có vấn đề
            messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

        finally:
            # Đóng kết nối
            if conn:
                conn.close()
    def reset_data(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_RoomType.set("")
# Chạy ứng dụng
if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()