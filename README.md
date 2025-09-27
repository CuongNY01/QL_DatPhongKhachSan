Chương 2: Xây dựng chương trình 
2.1. Phân tích hệ thống. 
2.1.1. Actor 
− Nhân viên (Employee): 
+ Mô tả: Người sử dụng hệ thống để thực hiện các nghiệp vụ quản lý hàng ngày của khách sạn. 
+ Quyền hạn: 
▪	Quản lý thông tin phòng (thêm, sửa, xóa, tìm kiếm). 
▪	Quản lý thông tin nhân viên (thêm, sửa, xóa, tìm kiếm). 
▪	Xem và tạo báo cáo (doanh thu, thống kê, ...). 
▪	Quản lý thông tin khách hàng (thêm, sửa, xóa, tìm kiếm). ▪ 	Thực hiện đặt phòng và trả phòng cho khách hàng. 
− Khách hàng (Customer): 
+ Mô tả: Đối tượng được quản lý thông tin trong hệ thống. Khách hàng không trực tiếp sử dụng hệ thống, nhưng thông tin của họ được sử dụng để phục vụ cho các nghiệp vụ quản lý. 
+ Quyền hạn: Không có quyền truy cập trực tiếp vào hệ thống. 
 
2.1.2. Các usecase 
− Biểu đồ use case tổng quát
  
Hình 2.1 Biểu đồ use case tổng quát 
 
 	 
 
Biểu đồ use case quản lý phòng 
 
  
Hình 2.2 Biểu đồ use case quản lý phòng 
 	 
Case: Quản lý phòng 
Use Case 	Quản lý phòng 
Tác nhân 	Nhân viên 
Mô tả 	Cho phép nhân viên thực hiện các thao tác thêm, sửa, xóa, tìm kiếm thông tin phòng. 
Điều kiện tiên quyết 	Nhân viên đã đăng nhập thành công vào hệ thống. 
Luồng chính  	1.	Nhân viên chọn chức năng "Quản lý phòng". 
2.	Hệ thống hiển thị danh sách phòng hiện có. 
3.	Nhân viên chọn một trong các thao tác: Thêm, Sửa, Xóa, Tìm kiếm. 
4.	Tùy thuộc vào thao tác, hệ thống hiển thị form tương ứng hoặc thực hiện tìm kiếm. 
5.	Nhân viên nhập/chọn thông tin cần thiết và xác nhận. 
6.	Hệ thống thực hiện thao tác và cập nhật danh sách phòng. 
Luồng 	thay 
thế  	-	Thông tin nhập không hợp lệ: Hệ thống hiển thị thông báo lỗi và yêu cầu nhập lại. 
-	Không tìm thấy phòng: Hệ thống hiển thị thông báo không tìm thấy. 
Điều kiện 	Thông tin phòng được cập nhật trong cơ sở dữ liệu. 
Yêu cầu 	- Hệ thống phải đảm bảo tính toàn vẹn dữ liệu. - Giao diện phải dễ sử dụng và thân thiện. 
 
 	 
Biểu đồ use case quản lý nhân viên 
  
Hinh2.3 Biểu đồ use case quản lý nhân viên 
 	 
Case: Quản lý nhân viên 
Tên Use Case 	Quản lý nhân viên 
Tác nhân 	Nhân viên 
Mô tả 	Cho phép nhân viên có quyền quản lý thực hiện các thao tác thêm, sửa, xóa, tìm kiếm thông tin nhân viên. 
Điều 	kiện 
tiên quyết 	Quản lý đã đăng nhập thành công vào hệ thống với quyền quản trị. 
Luồng chính   	1.	Quản lý chọn chức năng "Quản lý nhân viên". 
2.	Hệ thống hiển thị danh sách nhân viên hiện có. 
3.	Quản lý chọn một trong các thao tác: Thêm, Sửa, Xóa, Tìm kiếm. 
4.	Tùy thuộc vào thao tác, hệ thống hiển thị form tương ứng hoặc thực hiện tìm kiếm. 
5.	Quản lý nhập/chọn thông tin cần thiết và xác nhận. 
6.	Hệ thống thực hiện thao tác và cập nhật danh sách nhân viên. 
Luồng 	thay 
thế   	-	Thông tin nhập không hợp lệ: Hệ thống hiển thị thông báo lỗi và yêu cầu nhập lại. 
-	Không tìm thấy nhân viên: Hệ thống hiển thị thông báo không tìm thấy. 
Điều kiện 	Thông tin nhân viên được cập nhật trong cơ sở dữ liệu. 
Yêu cầu 	- Hệ thống phải đảm bảo tính bảo mật của thông tin nhân viên. //- Hệ thống phải có cơ chế phân quyền rõ ràng. 
 
 	 
Biểu đồ use case quản lý khách hàng 
  
Hình2.4 Biểu đồ use case quản lý khách hàng 
 	 
Case: Quản lý khách hàng 
Use Case 	Quản lý khách hàng 
Tác nhân 	Nhân viên 
Mô tả 	Cho phép nhân viên thực hiện các thao tác thêm, sửa, xóa, tìm kiếm thông tin khách hàng. 
Điều kiện tiên quyết 	Nhân viên đã đăng nhập thành công vào hệ thống. 
Luồng chính  	1.	Nhân viên chọn chức năng "Quản lý khách hàng". 
2.	Hệ thống hiển thị danh sách khách hàng hiện có. 
3.	Nhân viên chọn một trong các thao tác: Thêm, Sửa, Xóa, Tìm kiếm. 
4.	Tùy thuộc vào thao tác, hệ thống hiển thị form tương ứng hoặc thực hiện tìm kiếm. 
5.	Nhân viên nhập/chọn thông tin cần thiết và xác nhận. 
6.	Hệ thống thực hiện thao tác và cập nhật danh sách khách hàng. 
Luồng 	thay 
thế  	-	Thông tin nhập không hợp lệ: Hệ thống hiển thị thông báo lỗi và yêu cầu nhập lại. 
-	Không tìm thấy khách hàng: Hệ thống hiển thị thông báo không tìm thấy. 
Điều kiện 	Thông tin khách hàng được cập nhật trong cơ sở dữ liệu. 
Yêu cầu 	- Hệ thống phải đảm bảo tính toàn vẹn dữ liệu. - Giao diện phải dễ sử dụng và thân thiện. 
 
 	 
Biểu đồ use case quản lý đặt phòng 
 
  
Hình2.5 Biểu đồ use case quản lý đặt phòng 
 
Tên Use Case 	Quản lý đặt phòng 
Tác nhân 	Nhân viên 
Mô tả 	Cho phép nhân viên thực hiện các thao tác liên quan đến quản lý đặt phòng: tạo đặt phòng, sửa đổi đặt phòng, hủy đặt phòng, và tìm kiếm đặt phòng. 
Điều kiện tiên quyết 	Nhân viên đã đăng nhập thành công vào hệ thống. 
Luồng chính 	1. Nhân viên chọn chức năng "Quản lý đặt phòng". 
 
	2.	Hệ thống hiển thị giao diện quản lý đặt phòng (danh sách đặt phòng hiện có, các tùy chọn thao tác). 
3.	Nhân viên chọn một thao tác: "Tạo đặt phòng", "Sửa đặt phòng", "Hủy đặt phòng", "Tìm kiếm đặt phòng". 
4.	Tùy thuộc vào thao tác được chọn: 
*	Tạo đặt phòng: Hệ thống hiển thị form tạo đặt phòng. Nhân viên nhập thông tin (khách hàng, phòng, ngày đến, ngày đi, số lượng người, các yêu cầu đặc biệt). Hệ thống kiểm tra tính hợp lệ của dữ liệu. Nhân viên xác nhận tạo đặt phòng. Hệ thống tạo đặt phòng mới trong cơ sở dữ liệu. 
*	Sửa đặt phòng: Hệ thống hiển thị form sửa đặt phòng với thông tin hiện tại. Nhân viên sửa đổi thông tin cần thiết. Hệ thống kiểm tra tính hợp lệ của dữ liệu. Nhân viên xác nhận sửa đổi. Hệ thống cập nhật thông tin đặt phòng trong cơ sở dữ liệu. 
*	Hủy đặt phòng: Hệ thống yêu cầu xác nhận hủy đặt phòng. Nhân viên xác nhận. Hệ thống cập nhật trạng thái đặt phòng thành "Đã hủy" trong cơ sở dữ liệu. 
*	Tìm kiếm đặt phòng: Hệ thống hiển thị form tìm kiếm. Nhân viên nhập tiêu chí tìm kiếm (ví dụ: theo tên khách hàng, số điện thoại, số phòng, ngày đến). Hệ thống hiển thị kết quả tìm kiếm. 
Luồng 	thay 
thế 	*	Dữ liệu nhập không hợp lệ: Hệ thống hiển thị thông báo lỗi và yêu cầu nhập lại.  
*	Không tìm thấy đặt phòng: Hệ thống hiển thị thông báo không tìm thấy. 
Điều kiện 	Thông tin đặt phòng được cập nhật chính xác trong cơ sở dữ liệu. 
Yêu cầu 	*	Hệ thống phải đảm bảo tính toàn vẹn dữ liệu.  
*	Giao diện phải dễ sử dụng và thân thiện  
 
− Biểu đồ use case quản lý hóa đơn
  
Hình2.6 Biểu đồ use case quản lý hóa đơn 
 
 
Tên 	Use 
Case 	Quản lý hóa đơn  
Tác nhân 	Nhân viên 
Mô tả 	Cho phép nhân viên thực hiện các thao tác liên quan đến quản lý hóa đơn: tạo hóa đơn, xem hóa đơn, in hóa đơn, cập nhật trạng thái thanh toán. 
Điều 	kiện 
tiên quyết 	Đặt phòng đã được tạo và có thể đã hoàn thành (khách hàng đã check-out). Nhân viên đã đăng nhập thành công vào hệ thống. 
Luồng chính 	1.	Nhân viên chọn chức năng "Quản lý hóa đơn". 
2.	Hệ thống hiển thị giao diện quản lý hóa đơn (danh sách hóa đơn, các tùy chọn thao tác). 
	3.	Nhân viên chọn một thao tác: "Tạo hóa đơn", "Xem hóa đơn", "In hóa đơn", "Cập nhật trạng thái thanh toán". 
4.	Tùy thuộc vào thao tác được chọn 
*	Tạo hóa đơn: Hệ thống hiển thị danh sách các đặt phòng chưa có hóa đơn. Nhân viên chọn một đặt phòng. Hệ thống tự động tính toán tổng tiền dựa trên thông tin đặt phòng (giá phòng, số đêm, các dịch vụ phát sinh). Nhân viên có thể điều chỉnh các mục chi phí (ví dụ: thêm giảm giá). Nhân viên xác nhận tạo hóa đơn. Hệ thống tạo hóa đơn mới trong cơ sở dữ liệu, liên kết với đặt phòng. 
*	Xem hóa đơn: Nhân viên chọn một hóa đơn từ danh sách. Hệ thống hiển thị chi tiết hóa đơn (thông tin khách hàng, thông tin đặt phòng, các khoản chi phí, tổng tiền, trạng thái thanh toán). 
*	Cập nhật trạng thái thanh toán: Nhân viên cập nhật trạng thái thanh toán của hóa đơn (ví dụ: "Đã thanh toán", "Chưa thanh toán", "Thanh toán một phần"). 
Luồng thay thế 	*	Không tìm thấy đặt phòng/hóa đơn: Hệ thống hiển thị thông báo không tìm thấy.  
*	Lỗi tính toán: Hệ thống hiển thị thông báo lỗi nếu có vấn đề trong quá trình tính toán tổng tiền. 
Điều kiện 	Hóa đơn được tạo và lưu trữ chính xác trong cơ sở dữ liệu. Trạng thái thanh toán được cập nhật chính xác. 
Yêu cầu 	*	Hệ thống phải đảm bảo tính chính xác của các tính toán.  * Giao diện phải dễ sử dụng và thân thiện. 
*	Hệ thống nên có cơ chế bảo mật thông tin hóa đơn 
*	Cần có khả năng tạo báo cáo về doanh thu từ hóa đơn. 
 
 	 
 
2.1.3 Biểu đồ tuần tự 
− Biểu đồ tuần tự chức năng quản lý phòng 
  
Hình 2.7 Biểu đồ tuần tự chức năng quản lý phòng 
 
 	 
 
Biểu đồ tuần tự chức năng quản lý khách hàng 
  
Hình2.8 Biểu đồ tuần tự chức năng quản lý khách hàng 
 
 
 	 
Biểu đồ tuần tự chức năng quản lý nhân viên 
  
Hình 2.9 Biểu đồ tuần tự chức năng quản lý nhân viên 
 
 	 
Biểu đồ tuần tự chức năng đặt phòng 
  
Hình 2.10 Biểu đồ tuần tự chức năng đặt phòng 
 
 	 
Biểu đồ tuần tự chức năng hóa đơn 
  
Hình 2.11 Biểu đồ tuần tự chức năng hóa đơn 
 
 
 
2.2. Các chức năng của hệ thống. 
2.2.1. Biểu đồ phân rã chức năng. 
  
Hình 2.12 Biểu đồ phân rã chức năng. 
 	 
2.2.2. Thiết kế sơ đồ quan hệ thực thể (ERD) 
 
  
Hình 2.13 Sơ đồ quan hệ thực thể (ERD) 
 
2.3. Thiết kế cơ sở dữ liệu. 
2.3.1. Cấu trúc từng bảng trong database 
- Bảng NhanVien (Nhân Viên) 
Cột 	Kiểu Dữ Liệu 	Mô Tả 
ID 	INTEGER 	Mã định danh duy nhất cho mỗi nhân viên 
HoTen 	VARCHAR(45) 	Họ và tên đầy đủ của nhân viên 
SDT 	VARCHAR(10) 	Số điện thoại của nhân viên 
GioiTinh 	VARCHAR(10) 	Giới tính nhân viên 
Username 	VARCHAR(45) 	Tên đăng nhập của nhân viên (phải là duy nhất) 
Email 	VARCHAR(45) 	Email của nhân viên 
Password 	VARCHAR(45) 	Mật khẩu của nhân viên (phải được mã hóa an toàn) 
 
- Bảng KhachHang (Khách Hàng) 
Cột 	Kiểu Dữ Liệu 	Mô Tả 
ID 	INTEGER 	Mã định danh duy nhất cho mỗi khách hàng 
Ten 	VARCHAR(45) 	Tên của khách hàng 
Ho 	VARCHAR(45) 	Họ của khách hàng 
GioiTinh 	VARCHAR(45) 	Giới tính của khách hàng 
MaBuuDien 	VARCHAR(45) 	Mã bưu điện 
SDT 	VARCHAR(45) 	Số điện thoại của khách hàng (phải là duy nhất) 
Email 	VARCHAR(45) 	Địa chỉ email của khách hàng (phải là duy nhất) 
QuocTich 	VARCHAR(45) 	Quốc tịch khách hàng 
CCCD 	INTEGER 	Số Căn Cước Công Dân của khách hàng (phải là duy nhất) 
DiaChi 	VARCHAR(45) 	Địa chi của khách hàng 
 
-    Bảng Phong (Phòng) 
Cột 	Kiểu Dữ Liệu 	Mô Tả 
ID 	INTEGER 	Mã định danh duy nhất cho mỗi phòng 
LoaiPhong 	VARCHAR(100) 	Loại phòng (ví dụ: Đơn, Đôi, VIP) 
GiaTien 	FLOAT 	Giá tiền một đêm cho phòng 
SoPhong 	INTERGER 	Số phòng (phải là duy nhất) 
TrangThai 	VARCHAR(100) 	Trạng thái phòng (Trống, Đang sử dụng, Đã đặt) 
 
 	 
- Bảng DatPhong (Đặt Phòng) 
Cột 	Kiểu Dữ Liệu 	Mô Tả 
ID 	INTEGER 	Mã định danh duy nhất cho mỗi lượt đặt phòng 
MaKH 	INTEGER 	Mã khách hàng (khóa ngoại liên kết với bảng KhachHang) 
MaPhong 	INTEGER 	Mã phòng (khóa ngoại liên kết với bảng Phong) 
MaNV 	INTEGER 	Mã nhân viên (khóa ngoại liên kết với bảng NhanVien) 
NgayNhanPhong 	DATE 	Ngày nhận phòng 
NgayTraPhong 	DATE 	Ngày trả phòng 
TrangThai 	VARCHAR(100) 	Trạng thái đặt phòng (Đang đặt, Đã nhận phòng, Đã hủy) 
 
 
- Bảng HoaDon (Hóa Đơn) 
Cột 	Kiểu Dữ Liệu 	Mô Tả 
ID 	INTEGER 	Mã định danh duy nhất cho mỗi hóa đơn 
MaDatPhong 	INTEGER 	Mã đặt phòng (khóa ngoại liên kết với bảng DatPhong) 
NgayLap 	DATE 	Ngày lập hóa đơn 
TongTien 	FLOAT 	Tổng tiền của hóa đơn 
TrangThai 	VARCHAR(100) 	Trạng thái thanh toán (Chưa thanh toán, Đã thanh toán) 
 
2.3.2. Biểu đồ lớp. 
  
Hình 2.14 Biểu đồ lớp 
 	 
2.4. Thiết kế giao diện. 
2.4.1. Giao diện đăng nhập 
 
  
Hình 2.14 Giao diện đăng nhập 
- Giao diện đăng nhập chứa entry_username và entry_password để nhập thông tin đăng nhập, button_login dùng để xác nhận thông tin người dùng: 
o	Nếu thông tin đăng nhập hợp lệ, đúng cho phép truy cập trang chủ 
(hotel.py). 
o	Nếu thông tin đăng nhập không hợp lệ, sai thông tin người dùng thì hiển thị lỗi để người dùng biết sai ở đâu 
 	 
2.4.2. Trang chủ 
 
  
Hình 2.15 Giao diện trang chủ 
 
 
2.4.3. 	n quản lý khách hàng 
  
Hình 2.16 Giao diện quản lý khách hàng 
 
 	 
2.4.4. 	n quản lý phòng 
 
  
Hình 2.17 Giao diện quản lý phòng 
 
 	 
2.4.5. 	n đặt phòng 
 
  
	Hình 2.18 Giao diện đặt phòng 	 
 
2.4.6.	n quản lý nhân viên 
  
Hình 2.19 Giao diện quản lý nhân viên 
 	 
2.4.7. 	n trả phòng (hóa đơn) 
 
  
Hình 2.20 Giao diện trả phòng (hóa đơn) 
 
 	 
2.4.7. 	n báo cáo 
 
  
Hình 2.20 Giao diện báo cáo 
 
 
Chương 3: Kết quả thực nghiệm 
3.1 Quản lý khách hàng 
  
 
-	Hiển thị danh sách Khách hàng trong hệ thống 
-	Người dùng có thể thêm, sửa, xóa, tìm kiếm Khách hàng  
  
-	Người dùng nhập tên , họ , giới tính , mã bưu điện , số điện thoại ,email , quốc tịch , loại id , số id, địa chỉ 
-	Sau khi nhập xong nhấn Thêm dữ liệu khách hàng sẽ được lưu vào hệ thống 
  
Thông báo đã thêm khách hàng thành công 
  
Dữ liệu hiển thị trong danh sách khách hàng 
-	Người dùng chọn một khách hàng từ danh sách rồi thay đổi thông tin khách hàng sau đó nhấn Sửa  
  
Chọn một khách hàng trong danh sách 
  
Thông báo đã sửa khách hàng thành công 
 
-	Người dùng chọn một khách hàng và nhấn "Xóa". 
-	Hệ thống yêu cầu xác nhận trước khi xóa. 
  
 
  
-	Người dùng nhập số điện thoại khách hàng hoặc mã khách hàng để tìm kiếm khách hàng 
  
 
3.2 Quản lý phòng 
  
 
-	Hiển thị danh sách Phòng trong hệ thống 
-	Người dùng có thể thêm, sửa, xóa, tìm kiếm Phòng 
 
  
-	Người dùng nhập ID, số phòng, loại phòng, hạng phòng  
-	Sau khi nhập xong nhấn Thêm dữ liệu Phòng sẽ được lưu vào hệ thống 
  
Thông báo thêm Phòng thành công 
  
Dữ liệu hiển thị trong danh sách Phòng 
 
-	Người dùng chọn một Phòng từ danh sách rồi thay đổi thông Phòng sau đó nhấn Sửa  
  
Chọn một phòng trong danh sách 
  
Thông báo cập nhật thành công 
 
-	Người dùng chọn một khách hàng và nhấn "Xóa". 
-	Hệ thống yêu cầu xác nhận trước khi xóa. 
  
 
  
Thông báo xóa Phòng thành công 
-	Người dùng nhập ID phòng để tìm kiếm 
  
 
3.3 Quản lý nhân viên 
-	Chức năng thêm Nhân viên 
  
Nhập thông tin Nhân viên  
 
  
Thông báo thêm Nhân viên thành công 
  
Danh sách Nhân viên sau khi thêm 
-	Chức năng sửa Nhân viên 
 
 
 
 
Chọn một nhân viên để sửa 
  
Thông báo sửa nhân viên thành công 
-Chức năng xóa nhan viên 
  
Thông báo bạn có muốn xóa 
  
Đã xóa  nhân viên thành công 
-	Nhập ID nhân viên để tìm kiếm 
  
 
3.4 Đặt phòng 
-	Chức năng thêm đặt phòng 
  
Nhập thông tin đặt phòng 
  
Thông báo thêm đặt phòng thành công 
-	Chức năng sửa đặt phòng 
  
Chọn một đặt phòng để sửa 
 
  
Thông báo sửa đặt phòng thành công 
-	Chức năng xóa đặt phòng 
  
Chọn một đặt phòng muốn xóa 
  
Thông báo có chắc muốn xóa đặt phòng 
 
 
 
Thông báo xóa đặt phòng thành công 
-	Chức năng tìm kiếm 
Nhập số điện thoại để tìm kiếm 
  
 
 
 
3.5 Trả phòng  
 
  
Chọn một đặt phòng 
 
  
Thông báo trả phòng thành công 
 
  
 
Danh sách đặt phòng sau khi trả phòng 
 	 
3.6 Báo cáo   
-	Báo cáo khách hàng 
  
 
-	Báo cáo phòng 
  
 
 
 
KẾT LUẬN 
Qua quá trình nghiên cứu và thực hiện đề tài "Xây dựng phần mềm quản lý phòng khách sạn", nhóm em đã hoàn thành các mục tiêu đề ra và đạt được những kết quả đáng kể. Phần mềm được phát triển bằng ngôn ngữ Python với sự hỗ trợ của thư viện Tkinter và hệ quản trị cơ sở dữ liệu SQLite, đáp ứng được các yêu cầu cơ bản của một hệ thống quản lý phòng khách sạn hiện đại. 
Những kết quả đạt được: - Thiết kế hệ thống: 
+ Hệ thống được thiết kế với các chức năng chính như quản lý khách hàng, quản lý phòng, quản lý nhân viên, đặt phòng, trả phòng và báo cáo. Các chức năng này được phân tích kỹ lưỡng thông qua các biểu đồ use case, biểu đồ tuần tự và biểu đồ phân rã chức năng. + Cơ sở dữ liệu được thiết kế chặt chẽ với các bảng như KhachHang, Phong, NhanVien, DatPhong, và HoaDon, đảm bảo tính toàn vẹn và nhất quán dữ liệu. 
- Giao diện người dùng: 
+ Giao diện được thiết kế đơn giản, dễ sử dụng và thân thiện với người dùng. Các chức năng được phân chia rõ ràng, giúp nhân viên dễ dàng thao tác và quản lý thông tin. 
+ Các thông báo lỗi và cảnh báo được hiển thị rõ ràng, giúp người dùng nhận biết và xử lý các vấn đề phát sinh một cách nhanh chóng. 
− Tính năng nổi bật: 
+ Quản lý khách hàng: Cho phép thêm, sửa, xóa và tìm kiếm thông tin khách hàng một cách dễ dàng. 
+ Quản lý phòng: Hỗ trợ quản lý thông tin phòng, bao gồm loại phòng, giá cả, và trạng thái phòng. 
+ Đặt phòng và trả phòng: Hỗ trợ quy trình đặt phòng và trả phòng, tính toán tự động số ngày ở và tổng chi phí. 
+ Báo cáo: Cung cấp các báo cáo về khách hàng, phòng và doanh thu, giúp quản lý khách sạn dễ dàng theo dõi hoạt động kinh doanh. 
Hạn chế và hướng phát triển: 
− Hạn chế:  Chưa tích hợp các tính năng nâng cao như quản lý dịch vụ đi kèm (dịch vụ ăn uống, spa, v.v.) hoặc tích hợp thanh toán trực tuyến. 
− Hướng phát triển: 
+ Trong tương lai, nhóm em sẽ tiếp tục phát triển hệ thống bằng cách tích hợp thêm các tính năng nâng cao như quản lý dịch vụ, hỗ trợ đa ngôn ngữ, và tích hợp các phương thức thanh toán trực tuyến. 
+ Ngoài ra, hệ thống có thể được mở rộng để hỗ trợ quản lý nhiều chi nhánh khách sạn khác nhau, giúp quản lý tập trung và hiệu quả hơn. Kết luận chung: 
Phần mềm quản lý phòng khách sạn mà nhóm em xây dựng đã đáp ứng được các yêu cầu cơ bản của một hệ thống quản lý hiện đại, giúp tối ưu hóa quy trình quản lý và nâng cao hiệu quả hoạt động của khách sạn. Với những kết quả đạt được, nhóm em hy vọng rằng phần mềm này sẽ góp phần vào sự phát triển của ngành dịch vụ lưu trú tại Việt Nam, đồng thời là nền tảng để tiếp tục nghiên cứu và phát triển các ứng dụng công nghệ thông tin trong tương lai. 
 
 	  
TÀI LIỆU THAM KHẢO 
[1]	Giáo trình Lập Trình Ứng Dụng Với Python – Khoa Công nghệ thông tin – 
Trường Đại học công nghệ Đông Á  
(http://elearning.eaut.edu.vn/course/view.php?id=1723) 
[2]	Hướng dẫn học Python cơ bản 
(https://www.w3schools.com/python/default.asp ) 
[3]	https://luanvan.net.vn/luan-van/phan-tich-thiet-ke-he-thong-quan-ly-giangday-cua-giang-vien-tai-truong-dai-hoc-cong-nghiep-ha-noi-46469/ 
 
