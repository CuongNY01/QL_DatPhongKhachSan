from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import sqlite3
from tkinter import messagebox

class Checkout:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng khách sạn")
        self.root.geometry("1050x600+230+125")
        self.var_roomcategory = StringVar()
        self.var_conatct = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomclass = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Phòng khách sạn",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=10, width=410, height=480)
        lbl_cust_contact = Label(labelframeleft, text="SĐT Khách hàng : ", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_conatct, font=("Arial", 13, "bold"), width=13)
        enty_contact.grid(row=0, column=1, sticky=W)

        check_in_date = Label(labelframeleft, font=("arial", 12, "bold"), text="Ngày nhận phòng:", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("arial", 13, "bold"), width=20)
        txtcheck_in_date.grid(row=1, column=1)

        lbl_Check_out = Label(labelframeleft, font=("arial", 12, "bold"), text="Ngày trả phòng:", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=20)
        txt_Check_out.grid(row=2, column=1)

        label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Loại phòng:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = sqlite3.connect("quanlyphongkhachsan.db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT RoomType FROM details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=18, state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        label_RoomClass = Label(labelframeleft, font=("arial", 12, "bold"), text="Hạng phòng:", padx=2, pady=6)
        label_RoomClass.grid(row=4, column=0, sticky=W)

        conn = sqlite3.connect("quanlyphongkhachsan.db")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT RoomClass FROM details")
        ided = my_cursor.fetchall()

        combo_RoomClass = ttk.Combobox(labelframeleft, textvariable=self.var_roomclass, font=("arial", 12, "bold"), width=18, state="readonly")
        combo_RoomClass["value"] = ided
        combo_RoomClass.current(0)
        combo_RoomClass.grid(row=4, column=1)

        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Số phòng:", padx=2, pady=6)
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

        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), text="Số ngày ở", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=20)
        txtNoOfDays.grid(row=6, column=1)

        lblPaidTax = Label(labelframeleft, font=("arial", 12, "bold"), text="Thuế:", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=20)
        txtPaidTax.grid(row=7, column=1)

        lblSubTotal = Label(labelframeleft, font=("arial", 12, "bold"), text="Tổng phụ:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=("arial", 13, "bold"), width=20)
        txtSubTotal.grid(row=8, column=1)

        lblTotalCost = Label(labelframeleft, font=("arial", 12, "bold"), text="Tổng chi phí:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=("arial", 13, "bold"), width=20)
        txtTotalCost.grid(row=9, column=1)

        btnBill = Button(labelframeleft, text="Bill", command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnDelete = Button(btn_frame, text="Trả phòng", command=self.checkout_room, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Làm mới", command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        img3 = Image.open(r"PHONG.jpg")
        img3 = img3.resize((600, 250), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=420, y=10, width=600, height=300)

        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Xem thông tin khách hàng và tìm kiếm",
                                 font=("arial", 12, "bold"))
        Table_Frame.place(x=420, y=280, width=620, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Tìm kiếm:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.serch_var, font=("arial", 12, "bold"), width=6,
                                    state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_serch = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_serch, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=620, height=250)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,
                                       columns=("contact", "checkin", "checkout", "roomtype", "roomclass", "roomvailable"),
                                       xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="SĐT Khách hàng")
        self.room_table.heading("checkin", text="Ngày nhận phòng")
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

    def checkout_room(self):
        if self.var_conatct.get() == "":
            messagebox.showerror("Error", "Vui lòng nhập số điện thoại khách hàng", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("quanlyphongkhachsan.db")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Contact, check_in, check_out, roomtype, roomclass, roomavailable FROM room WHERE contact=?", (self.var_conatct.get(),))
                room_data = my_cursor.fetchone()

                if room_data is None:
                    messagebox.showerror("Error", "Không tìm thấy thông tin đặt phòng", parent=self.root)
                else:
                    contact, check_in, check_out, roomtype, roomclass, roomavailable = room_data

                    check_in_date = datetime.strptime(check_in, "%d/%m/%Y")
                    check_out_date = datetime.strptime(check_out, "%d/%m/%Y")
                    num_of_days = (check_out_date - check_in_date).days

                    price_per_day = self.get_room_price(roomtype,roomclass)

                    total_amount = price_per_day * num_of_days

                    insert_query = """
                        INSERT INTO doanhthu (roomavailable, contact, check_in, check_out, roomtype, roomclass, price_per_day, num_of_days, total_amount)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
                    my_cursor.execute(insert_query, (roomavailable, contact, check_in, check_out, roomtype,roomclass, price_per_day, num_of_days, total_amount))

                    delete_query = "DELETE FROM room WHERE contact=?"
                    my_cursor.execute(delete_query, (self.var_conatct.get(),))

                    conn.commit()

                    messagebox.showinfo("Success", "Phòng đã được trả thành công", parent=self.root)
                    self.fetch_data()

            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong: {str(e)}", parent=self.root)
            finally:
                if conn:
                    conn.close()

    def get_room_price(self, roomtype, roomclass):
        room_prices = {
            ("Đơn", "Thường"): 300,
            ("Đơn", "VIP"): 500,
            ("Đôi", "Thường"): 500,
            ("Đôi", "VIP"): 800,
        }

        return room_prices.get((roomtype, roomclass), 0)

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()

        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")

        self.var_noofdays.set(abs(outDate - inDate).days)

        room_prices = {
            "Đơn": {"Thường": 300, "VIP": 500},
            "Đôi": {"Thường": 500, "VIP": 800}
        }

        room_type = self.var_roomtype.get()
        room_category = self.var_roomclass.get()

        if room_type in room_prices and room_category in room_prices[room_type]:
            room_price = room_prices[room_type][room_category]
        else:
            messagebox.showerror("Error", "Loại phòng hoặc hạng phòng không hợp lệ", parent=self.root)
            return

        total_cost = room_price * float(self.var_noofdays.get())

        tax = total_cost * 0.09

        total_with_tax = total_cost + tax

        self.var_paidtax.set(f"{tax:.2f} VND")
        self.var_actualtotal.set(f"{total_cost:.2f} VND")
        self.var_total.set(f"{total_with_tax:.2f} VND")

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

    def reset(self):
        self.var_conatct.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomavailable.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

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
    obj = Checkout(root)
    root.mainloop()