from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from report import ReportWindow
from employee import Employee
from checkout import Checkout
class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng khách sạn")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open("hotel.jpg")
        img1 = img1.resize((1550, 90))
        self.photoimg = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=90)

        img2 = Image.open(r"logo.jpg")
        img2 = img2.resize((230, 90))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=140, height=90)

        lbl_title = Label(self.root,text=" HỆ THỐNG QUẢN LÝ PHÒNG KHÁCH SẠN ",font=("times new roman", 25 ,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x =0 ,y =90 , width =1280, height = 40)

        main_frame =Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x= 0,y =90, width = 1550,height =620)

        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"),
                         bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=260)

        cust_btn = Button(btn_frame, text="KHÁCH HÀNG",command=self.cust_details, width=22,font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ĐẶT PHÒNG",command=self.roombooking, width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        roomout_btn = Button(btn_frame, text="TRẢ PHÒNG",command=self.checkout, width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        roomout_btn.grid(row=2, column=0, pady=1)

        details_btn = Button(btn_frame, text="PHÒNG",command=self.detail_sroom, width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=3, column=0, pady=1)

        employes_btn = Button(btn_frame, text="NHÂN VIÊN",command=self.employee_sroom, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        employes_btn.grid(row=4, column=0, pady=1)

        report_btn = Button(btn_frame, text="BÁO CÁO",command=self.report, width=22,font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=5, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.logout, width=22,font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=6, column=0, pady=1)


        img3 = Image.open(r"hotel3.jpg")
        img3 = img3.resize((1100, 650), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1100, height=650)

        img4 = Image.open(r"hotel3.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=290, width=230, height=130)

        img5 = Image.open(r"hotel3.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel()
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel()
        self.app = Roombooking(self.new_window)

    def detail_sroom(self):
        self.new_window = Toplevel()
        self.app = DetailsRoom(self.new_window)

    def employee_sroom(self):
        self.new_window = Toplevel()
        self.app = Employee(self.new_window)
    def checkout(self):
        self.new_window = Toplevel()
        self.app = Checkout(self.new_window)
    def logout(self):
        self.root.destroy()

    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = ReportWindow(self.new_window)
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
