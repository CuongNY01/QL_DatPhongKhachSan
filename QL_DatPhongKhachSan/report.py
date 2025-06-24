from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from datetime import datetime

class ReportWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Báo cáo Thống Kê")
        self.root.geometry("1050x600+230+125")

        main_frame = Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        title_label = Label(main_frame, text="Báo Cáo Thống Kê", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        revenue_frame = LabelFrame(main_frame, text="Thống Kê Doanh Thu", font=("Arial", 12))
        revenue_frame.pack(fill="x", pady=10)

        self.total_revenue_label = Label(revenue_frame, text="Tổng Doanh Thu: 0.0 VND", font=("Arial", 12))
        self.total_revenue_label.pack(pady=5)

        monthly_revenue_frame = LabelFrame(revenue_frame, text="Doanh Thu Theo Tháng", font=("Arial", 12))
        monthly_revenue_frame.pack(fill="x", pady=5)

        self.monthly_revenue_tree = ttk.Treeview(monthly_revenue_frame, columns=("Month", "Revenue"), show="headings")
        self.monthly_revenue_tree.heading("Month", text="Tháng")
        self.monthly_revenue_tree.heading("Revenue", text="Doanh Thu (VND)")
        self.monthly_revenue_tree.pack(fill="x")

        room_stats_frame = LabelFrame(main_frame, text="Thống Kê Phòng", font=("Arial", 12))
        room_stats_frame.pack(fill="x", pady=10)

        self.total_rooms_label = Label(room_stats_frame, text="Tổng số phòng: 0", font=("Arial", 12))
        self.total_rooms_label.pack(pady=2)
        self.booked_rooms_label = Label(room_stats_frame, text="Phòng đã đặt: 0", font=("Arial", 12))
        self.booked_rooms_label.pack(pady=2)
        self.available_rooms_label = Label(room_stats_frame, text="Phòng còn trống: 0", font=("Arial", 12))
        self.available_rooms_label.pack(pady=2)

        customer_stats_frame = LabelFrame(main_frame, text="Thống Kê Khách Hàng", font=("Arial", 12))
        customer_stats_frame.pack(fill="x", pady=10)

        self.total_customers_label = Label(customer_stats_frame, text="Tổng số khách hàng: 0", font=("Arial", 12))
        self.total_customers_label.pack(pady=2)
        self.booked_customers_label = Label(customer_stats_frame, text="Số khách hàng đã đặt phòng: 0", font=("Arial", 12))
        self.booked_customers_label.pack(pady=2)

        top_customers_frame = LabelFrame(customer_stats_frame, text="Top 5 Khách hàng đặt phòng nhiều nhất:", font=("Arial", 12))
        top_customers_frame.pack(fill="x", pady=5)

        self.top_customers_tree = ttk.Treeview(top_customers_frame, columns=("Customer", "Bookings"), show="headings")
        self.top_customers_tree.heading("Customer", text="Tên Khách Hàng")
        self.top_customers_tree.heading("Bookings", text="Số Lần Đặt Phòng")
        self.top_customers_tree.pack(fill="x")

        self.update_reports()

    def update_reports(self):
        try:
            conn = sqlite3.connect("quanlyphongkhachsan.db")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT SUM(total_amount) FROM doanhthu")
            total_revenue = my_cursor.fetchone()[0]
            if total_revenue is None:
                total_revenue = 0
            self.total_revenue_label.config(text=f"Tổng Doanh Thu: {total_revenue:,.1f} VND")

            my_cursor.execute("""
                SELECT strftime('%Y-%m', check_in), SUM(total_amount)
                FROM doanhthu
                GROUP BY strftime('%Y-%m', check_in)
            """)
            monthly_revenues = my_cursor.fetchall()
            for item in self.monthly_revenue_tree.get_children():
                self.monthly_revenue_tree.delete(item)
            for month, revenue in monthly_revenues:
                self.monthly_revenue_tree.insert("", "end", values=(month, f"{revenue:,.1f}"))

            my_cursor.execute("SELECT COUNT(*) FROM details")
            total_rooms = my_cursor.fetchone()[0]
            my_cursor.execute("SELECT COUNT(DISTINCT roomavailable) FROM room")
            booked_rooms = my_cursor.fetchone()[0]
            available_rooms = total_rooms - booked_rooms

            self.total_rooms_label.config(text=f"Tổng số phòng: {total_rooms}")
            self.booked_rooms_label.config(text=f"Phòng đã đặt: {booked_rooms}")
            self.available_rooms_label.config(text=f"Phòng còn trống: {available_rooms}")

            my_cursor.execute("SELECT COUNT(*) FROM customer")
            total_customers = my_cursor.fetchone()[0]
            my_cursor.execute("SELECT COUNT(DISTINCT contact) FROM room")
            booked_customers = my_cursor.fetchone()[0]

            self.total_customers_label.config(text=f"Tổng số khách hàng: {total_customers}")
            self.booked_customers_label.config(text=f"Số khách hàng đã đặt phòng: {booked_customers}")


            my_cursor.execute("""
                SELECT contact, COUNT(*) AS booking_count
                FROM room
                GROUP BY contact
                ORDER BY booking_count DESC
                LIMIT 5
            """)
            top_customers = my_cursor.fetchall()

            for item in self.top_customers_tree.get_children():
                self.top_customers_tree.delete(item)
            for contact, booking_count in top_customers:
                my_cursor.execute("SELECT Name FROM customer WHERE Mobile=?", (contact,))
                customer_name = my_cursor.fetchone()
                if customer_name:
                    self.top_customers_tree.insert("", "end", values=(customer_name[0], booking_count))
                else:
                    self.top_customers_tree.insert("", "end", values=("Không rõ", booking_count))

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật báo cáo: {str(e)}", parent=self.root)

        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = ReportWindow(root)
    root.mainloop()