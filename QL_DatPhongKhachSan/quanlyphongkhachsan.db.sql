BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS customer (
        Ref INT PRIMARY KEY,
        Name VARCHAR(45),
        Mother VARCHAR(45),
        Gender VARCHAR(45),
        PostCode VARCHAR(45),
        Mobile VARCHAR(45),
        Email VARCHAR(45),
        Nationality VARCHAR(45),
        Idproof VARCHAR(45),
        Idnumber VARCHAR(45),
        Address VARCHAR(45)
    );
CREATE TABLE IF NOT EXISTS "details" (
	"Floor"	VARCHAR(45),
	"RoomNo"	VARCHAR(45),
	"RoomType"	VARCHAR(45),
	"RoomClass"	VARCHAR(45),
	PRIMARY KEY("RoomNo")
);
CREATE TABLE IF NOT EXISTS nhanvien (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ho_ten TEXT NOT NULL,
                so_dien_thoai TEXT,
                gioi_tinh TEXT,
                email TEXT,
                tai_khoan TEXT UNIQUE NOT NULL,
                mat_khau TEXT NOT NULL
            );
CREATE TABLE IF NOT EXISTS "room" (
	"Contact"	VARCHAR(45),
	"check_in"	VARCHAR(45),
	"check_out"	VARCHAR(45),
	"roomtype"	VARCHAR(45),
	"roomclass"	VARCHAR(45),
	"roomavailable"	VARCHAR(45),
	PRIMARY KEY("roomavailable")
);
INSERT INTO "customer" ("Ref","Name","Mother","Gender","PostCode","Mobile","Email","Nationality","Idproof","Idnumber","Address") VALUES (5538,'Thang','Vu','Nam','123','12345','thang@gmail.com','Việt Nam','CCCD','1234567891','1234567'),
 (3320,'Cuong','Ha','Nam','123','9999','dáyhgabs','Việt Nam','CCCD','123450','0876'),
 (9884,'Thắng','Vũ','Nam','20000','9876541321','thang@gmail.com','Việt Nam','CCCD','123235623','Hà Nội'),
 (6753,'Khách hàng ','1','Nam','001','098326724','A@gmail.com','Việt Nam','CCCD','097239873221','YB'),
 (8745,'Khach Hang','4','Nam','1000','0987654321','A@gmaill.com','Việt Nam','CCCD','987329324','YB');
INSERT INTO "details" ("Floor","RoomNo","RoomType","RoomClass") VALUES ('1','P101','Đơn','VIP'),
 ('2','P102','Đôi','Thường'),
 ('3','P103','Đơn','VIP');
INSERT INTO "nhanvien" ("id","ho_ten","so_dien_thoai","gioi_tinh","email","tai_khoan","mat_khau") VALUES (1,'Vũ Đức Thắng','0987654321','Nam','thang@gmail.com','thang','1'),
 (2,'Cuong','09876','Nam','tyhasnd','cuong','1');
INSERT INTO "room" ("Contact","check_in","check_out","roomtype","roomclass","roomavailable") VALUES ('9999','12/12/2025','16/12/2025','Đơn','VIP','P102');
COMMIT;
