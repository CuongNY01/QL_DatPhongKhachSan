from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập hệ thống quản lý phòng khách sạn")
        self.root.geometry("550x500+0+0")

        bg_img = Image.open("hotel.jpg")
        bg_img = bg_img.resize((550, 500))
        self.bg_photoimg = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photoimg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=100, y=70, width=350, height=400)

        title_label = Label(login_frame, text="Đăng nhập", font=("times new roman", 30, "bold"), bg="white", fg="black")
        title_label.place(x=80, y=30)

        username_label = Label(login_frame, text="Tên đăng nhập", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username_label.place(x=30, y=100)

        self.username_entry = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.username_entry.place(x=30, y=130, width=270)

        password_label = Label(login_frame, text="Mật khẩu", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password_label.place(x=30, y=180)

        self.password_entry = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.password_entry.place(x=30, y=210, width=270)

        login_btn = Button(login_frame, text="Đăng nhập", command=self.login, font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        login_btn.place(x=30, y=270, width=270)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect("quanlyphongkhachsan.db")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM nhanvien WHERE tai_khoan = ? AND mat_khau = ?", (username, password))
        result = my_cursor.fetchone()

        if result:
            self.root.destroy()
            import hotel
            root = Tk()
            obj = hotel.HotelManagementSystem(root)
            root.mainloop()
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")

        my_cursor.close()
        conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()