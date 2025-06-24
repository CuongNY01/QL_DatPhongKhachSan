from tkinter import *
from PIL import Image, ImageTk
from  tkinter import ttk
import random
from time import strftime
from datetime import datetime
import sqlite3
from tkinter import messagebox
class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng khách sạn")
        self.root.geometry("1050x600+230+125")

        self.var_conatct = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomclass = StringVar()
        self.var_roomavailable = StringVar()
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Đặt phòng khách sạn",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=10, width=410, height=480)
        lbl_cust_contact = Label(labelframeleft, text="SĐT Khách hàng : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft,textvariable=self.var_conatct, font=("Arial", 13, "bold"), width=13)
        enty_contact.grid(row=0, column=1,sticky=W)

        btnFetcData = Button(labelframeleft, command=self.Fetch_contact,text="FetcData", font=("arial", 9, "bold"), bg="black", fg="gold",
                        width=10)
        btnFetcData.place(x= 260,y =4)

        check_in_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Ngày nhận phòng", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin, font=("arial", 13, "bold"), width=20)
        txtcheck_in_date.grid(row=1, column=1)

        check_out_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Ngày trả phòng", padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)

        txtcheck_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"),
                                     width=20)
        txtcheck_out_date.grid(row=2, column=1)

        label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Loại phòng:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = sqlite3.connect("quanlyphongkhachsan.db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT RoomType FROM details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=18, state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        label_RoomClass = Label(labelframeleft, font=("arial", 12, "bold"), text="Hạng phòng:", padx=2, pady=6)
        label_RoomClass.grid(row=4, column=0, sticky=W)

        conn = sqlite3.connect("quanlyphongkhachsan.db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT RoomClass FROM details")
        ided = my_cursor.fetchall()

        combo_RoomClass = ttk.Combobox(labelframeleft, textvariable=self.var_roomclass, font=("arial", 12, "bold"),
                                       width=18, state="readonly")
        combo_RoomClass["value"] = ided
        combo_RoomClass.current(0)
        combo_RoomClass.grid(row=4, column=1)

        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Số phòng", padx=2, pady=6)
        lblRoomAvailable.grid(row=5, column=0, sticky=W)

        conn = sqlite3.connect("quanlyphongkhachsan.db")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT RoomNo FROM details")
        rows = my_cursor.fetchall()
        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"),
                                      width=18, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=5, column=1)

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Thêm",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Sửa",command=self.update, font=("arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Xóa",command=self.mDelete,  font=("arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Làm mới",command=self.reset,  font=("arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        img3 = Image.open(r"PHONG.jpg")
        img3 = img3.resize((600, 250),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=420, y=10, width=600, height=300)


        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Xem phòng đặt và tìm kiếm",
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=420, y=280, width=620, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Tìm kiếm :", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.serch_var, font=("arial", 12, "bold"), width=6,
                                    state="readonly")
        combo_Search["value"] = ("Contact")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_serch = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_serch, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Tìm kiếm",command=self.search,  font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Hiển thị tất cả",command=self.fetch_data, font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)


        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=620, height=250)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,
                                               columns=("contact", "checkin", "checkout", "roomtype","roomclass", "roomvailable"),
                                               xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Số điện thoại")
        self.room_table.heading("checkin", text="Ngày nhân phòng")
        self.room_table.heading("checkout", text="Ngày trả phòng")
        self.room_table.heading("roomtype", text="Loại phòng")
        self.room_table.heading("roomclass", text="Hạng phòng")
        self.room_table.heading("roomvailable", text="Số phòng")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomclass", width=100)
        self.room_table.column("roomvailable", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_conatct.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:

                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "INSERT INTO room (contact, check_in,check_out, roomtype,roomclass, roomavailable) VALUES (?,?,?, ?, ?, ?)",
                    (
                        self.var_conatct.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomclass.get(),
                        self.var_roomavailable.get(),
                    ))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Thêm đặt phòng thành công !", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    def fetch_data(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT * FROM room")
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())

                for i in rows:
                    self.room_table.insert("", END, values=i)

        except Exception as e:
            print(f"Lỗi khi truy vấn dữ liệu: {e}")

        finally:
            if conn:
                conn.close()

    def get_cuersor(self, event=""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row = content["values"]

        self.var_conatct.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomclass.set(row[4])
        self.var_roomavailable.set(row[5])

    def update(self):
        if self.var_conatct.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                my_cursor.execute("""
                       UPDATE room
                       SET check_in=?,check_out=? ,roomtype=?,roomclass=?, roomavailable=?
                       WHERE Contact=?
                   """, (
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomclass.get(),
                    self.var_roomavailable.get(),
                    self.var_conatct.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Sửa thông tin đặt phòng thành công", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Bạn có chắc muốn xóa đặt phòng này ?",
                                      parent=self.root)

        if mDelete:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()
                query = "DELETE FROM room WHERE Contact=?"
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)

                conn.commit()

                messagebox.showinfo("Success", "Xóa đặt phòng thành công", parent=self.root)
                self.fetch_data()

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()
        else:
            return

    def reset(self):
        self.var_conatct.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomavailable.set("")
    def Fetch_contact(self):
        if self.var_conatct.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                query = "SELECT Name FROM customer WHERE Mobile=?"
                value = (self.var_conatct.get(),)
                my_cursor.execute(query, value)

                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "This number Not Found", parent=self.root)
                else:
                    showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                    showDataframe.place(x=455, y=55, width=300, height=180)

                    lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                    lblName.place(x=0, y=0)

                    lbl = Label(showDataframe, text=row[0],font=("arial", 12, "bold"))  #
                    lbl.place(x=90, y=0)
                    query = "SELECT Gender FROM customer WHERE Mobile=?"
                    value = (self.var_conatct.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblGender = Label(showDataframe, text="Giới tính:", font=("arial", 12, "bold"))
                    lblGender.place(x=0, y=30)

                    if row is not None:
                        lbl2 = Label(showDataframe, text=row[0],font=("arial", 12, "bold"))
                        lbl2.place(x=90, y=30)
                    else:
                        lbl2 = Label(showDataframe, text="N/A",font=("arial", 12, "bold"))
                        lbl2.place(x=90, y=30)


                    query = "SELECT Email FROM customer WHERE Mobile=?"
                    value = (self.var_conatct.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()

                    lblemail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                    lblemail.place(x=0, y=60)

                    if row is not None:
                        lbl3 = Label(showDataframe, text=row[0],font=("arial", 12, "bold"))
                        lbl3.place(x=90, y=60)
                    else:
                        lbl3 = Label(showDataframe, text="N/A",font=("arial", 12, "bold"))
                        lbl3.place(x=90, y=60)

                    query = "SELECT Nationality FROM customer WHERE Mobile=?"
                    value = (self.var_conatct.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                    lblNationality.place(x=0, y=90)
                    lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                    lbl4.place(x=90, y=90)

                    query = "SELECT Address FROM customer WHERE Mobile=?"
                    value = (self.var_conatct.get(),)
                    my_cursor.execute(query, value)
                    row = my_cursor.fetchone()
                    lbladdress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                    lbladdress.place(x=0, y=120)
                    lbl1 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                    lbl1.place(x=90, y=120)
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

            finally:
                if conn:
                    conn.close()

    # def total(self):
    #     inDate = self.var_checkin.get()
    #     outDate = self.var_checkout.get()
    #     inDate = datetime.strptime(inDate, "%d/%m/%Y")
    #     outDate = datetime.strptime(outDate, "%d/%m/%Y")
    #     self.var_noofdays.set(abs(outDate - inDate).days)
    #
    #     if (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "laxary"):
    #         q1 = float(300)
    #         q2 = float(700)
    #         q3 = float(self.var_noofdays.get())
    #         q4 = float(q1 + q2)
    #         q5 = float(q3 + q4)
    #         Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
    #         ST = "Rs." + str("%.2f" % ((q5)))
    #         TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
    #         self.var_paidtax.set(Tax)
    #         self.var_actualtotal.set(ST)
    #         self.var_total.set(TT)
    #     elif (self.var_meal.get() == "Launch" and self.var_roomtype.get() == "Single"):
    #         q1 = float(300)
    #         q2 = float(700)
    #         q3 = float(self.var_noofdays.get())
    #         q4 = float(q1 + q2)
    #         q5 = float(q3 + q4)
    #         Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
    #         ST = "Rs." + str("%.2f" % ((q5)))
    #         TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
    #         self.var_paidtax.set(Tax)
    #         self.var_actualtotal.set(ST)
    #         self.var_total.set(TT)
    #     elif (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Duplex"):
    #         q1 = float(500)
    #         q2 = float(1000)
    #         q3 = float(self.var_noofdays.get())
    #         q4 = float(q1 + q2)
    #         q5 = float(q3 + q4)
    #         Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
    #         ST = "Rs." + str("%.2f" % ((q5)))
    #         TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
    #         self.var_paidtax.set(Tax)
    #         self.var_actualtotal.set(ST)
    #         self.var_total.set(TT)

    def search(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()

            search_column = self.serch_var.get()
            search_value = self.txt_serch.get()
            query = f"SELECT * FROM room WHERE {search_column} LIKE ?"
            my_cursor.execute(query, (f"%{search_value}%",))
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())

                for i in rows:
                    self.room_table.insert("", END, values=i)
            else:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)

        finally:
            if conn:
                conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()