# Dự án: Xây dựng phần mềm quản lý phòng khách sạn

## Mục lục
1.  [Giới thiệu](#giới-thiệu)
2.  [Phân tích hệ thống](#phân-tích-hệ-thống)
    1.  [Actor](#actor)
    2.  [Use Case](#use-case)
    3.  [Biểu đồ tuần tự](#biểu-đồ-tuần-tự)
3.  [Các chức năng của hệ thống](#các-chức-năng-của-hệ-thống)
    1.  [Biểu đồ phân rã chức năng](#biểu-đồ-phân-rã-chức-năng)
    2.  [Thiết kế sơ đồ quan hệ thực thể (ERD)](#thiết-kế-sơ-đồ-quan-hệ-thực-thể-erd)
    3.  [Thiết kế cơ sở dữ liệu](#thiết-kế-cơ-sở-dữ-liệu)
    4.  [Biểu đồ lớp](#biểu-đồ-lớp)
4.  [Thiết kế giao diện](#thiết-kế-giao-diện)
5.  [Kết quả thực nghiệm](#kết-quả-thực-nghiệm)
6.  [Kết luận](#kết-luận)
    1.  [Những kết quả đạt được](#những-kết-quả-đạt-được)
    2.  [Hạn chế và hướng phát triển](#hạn-chế-và-hướng-phát-triển)

## 1. Giới thiệu

Đề tài "Xây dựng phần mềm quản lý phòng khách sạn" nhằm mục đích phát triển một hệ thống giúp tối ưu hóa các nghiệp vụ quản lý hàng ngày tại khách sạn. Phần mềm được thiết kế để quản lý hiệu quả thông tin khách hàng, phòng, nhân viên, đặt phòng, trả phòng và tạo các báo cáo cần thiết.

Dự án được phát triển bằng ngôn ngữ **Python** với sự hỗ trợ của thư viện **Tkinter** cho giao diện người dùng và hệ quản trị cơ sở dữ liệu **SQLite** để lưu trữ thông tin. Mục tiêu là cung cấp một công cụ quản lý đơn giản, thân thiện và đáng tin cậy cho nhân viên khách sạn.

## 2. Phân tích hệ thống

### 2.1. Actor

Hệ thống có hai tác nhân chính:

*   **Nhân viên (Employee):**
    *   **Mô tả:** Người sử dụng hệ thống để thực hiện các nghiệp vụ quản lý khách sạn hàng ngày.
    *   **Quyền hạn:**
        *   Quản lý thông tin phòng (thêm, sửa, xóa, tìm kiếm).
        *   Quản lý thông tin nhân viên (thêm, sửa, xóa, tìm kiếm).
        *   Xem và tạo báo cáo (doanh thu, thống kê).
        *   Quản lý thông tin khách hàng (thêm, sửa, xóa, tìm kiếm).
        *   Thực hiện đặt phòng và trả phòng cho khách hàng.

*   **Khách hàng (Customer):**
    *   **Mô tả:** Đối tượng được quản lý thông tin trong hệ thống. Khách hàng không trực tiếp sử dụng hệ thống, nhưng thông tin của họ được lưu trữ và sử dụng cho các nghiệp vụ quản lý.
    *   **Quyền hạn:** Không có quyền truy cập trực tiếp vào hệ thống.

### 2.2. Use Case

Hệ thống được thiết kế với các Use Case chính bao gồm:

*   **Biểu đồ Use Case tổng quát:** Mô tả tổng thể các chức năng mà hệ thống cung cấp và các tác nhân tương tác.
    *   *(Hình 2.1 Biểu đồ use case tổng quát - Đính kèm hình ảnh)*

*   **Use Case: Quản lý phòng**
    *   **Tác nhân:** Nhân viên
    *   **Mô tả:** Cho phép nhân viên thực hiện các thao tác thêm, sửa, xóa, tìm kiếm thông tin phòng.
    *   **Điều kiện tiên quyết:** Nhân viên đã đăng nhập thành công vào hệ thống.
    *   *(Hình 2.2 Biểu đồ use case quản lý phòng - Đính kèm hình ảnh)*

*   **Use Case: Quản lý nhân viên**
    *   **Tác nhân:** Nhân viên (có quyền quản lý)
    *   **Mô tả:** Cho phép nhân viên có quyền quản lý thực hiện các thao tác thêm, sửa, xóa, tìm kiếm thông tin nhân viên.
    *   **Điều kiện tiên quyết:** Nhân viên đã đăng nhập thành công vào hệ thống với quyền quản trị.
    *   *(Hình 2.3 Biểu đồ use case quản lý nhân viên - Đính kèm hình ảnh)*

*   **Use Case: Quản lý khách hàng**
    *   **Tác nhân:** Nhân viên
    *   **Mô tả:** Cho phép nhân viên thực hiện các thao tác thêm, sửa, xóa, tìm kiếm thông tin khách hàng.
    *   **Điều kiện tiên quyết:** Nhân viên đã đăng nhập thành công vào hệ thống.
    *   *(Hình 2.4 Biểu đồ use case quản lý khách hàng - Đính kèm hình ảnh)*

*   **Use Case: Quản lý đặt phòng**
    *   **Tác nhân:** Nhân viên
    *   **Mô tả:** Cho phép nhân viên thực hiện các thao tác liên quan đến quản lý đặt phòng: tạo, sửa đổi, hủy và tìm kiếm đặt phòng.
    *   **Điều kiện tiên quyết:** Nhân viên đã đăng nhập thành công vào hệ thống.
    *   *(Hình 2.5 Biểu đồ use case quản lý đặt phòng - Đính kèm hình ảnh)*

*   **Use Case: Quản lý hóa đơn**
    *   **Tác nhân:** Nhân viên
    *   **Mô tả:** Cho phép nhân viên thực hiện các thao tác liên quan đến quản lý hóa đơn: tạo, xem, in hóa đơn và cập nhật trạng thái thanh toán.
    *   **Điều kiện tiên quyết:** Đặt phòng đã được tạo và có thể đã hoàn thành (khách hàng đã check-out). Nhân viên đã đăng nhập thành công vào hệ thống.
    *   *(Hình 2.6 Biểu đồ use case quản lý hóa đơn - Đính kèm hình ảnh)*

### 2.3. Biểu đồ tuần tự

Các biểu đồ tuần tự minh họa luồng tương tác giữa các đối tượng trong hệ thống cho từng chức năng chính:

*   **Biểu đồ tuần tự chức năng quản lý phòng**
    *   *(Hình 2.7 Biểu đồ tuần tự chức năng quản lý phòng - Đính kèm hình ảnh)*
*   **Biểu đồ tuần tự chức năng quản lý khách hàng**
    *   *(Hình 2.8 Biểu đồ tuần tự chức năng quản lý khách hàng - Đính kèm hình ảnh)*
*   **Biểu đồ tuần tự chức năng quản lý nhân viên**
    *   *(Hình 2.9 Biểu đồ tuần tự chức năng quản lý nhân viên - Đính kèm hình ảnh)*
*   **Biểu đồ tuần tự chức năng đặt phòng**
    *   *(Hình 2.10 Biểu đồ tuần tự chức năng đặt phòng - Đính kèm hình ảnh)*
*   **Biểu đồ tuần tự chức năng hóa đơn**
    *   *(Hình 2.11 Biểu đồ tuần tự chức năng hóa đơn - Đính kèm hình ảnh)*

## 3. Các chức năng của hệ thống

### 3.1. Biểu đồ phân rã chức năng

Biểu đồ phân rã chức năng mô tả cấu trúc phân cấp các chức năng của hệ thống.
*   *(Hình 2.12 Biểu đồ phân rã chức năng - Đính kèm hình ảnh)*

### 3.2. Thiết kế sơ đồ quan hệ thực thể (ERD)

Sơ đồ quan hệ thực thể (ERD) thể hiện cấu trúc logic của cơ sở dữ liệu, các thực thể và mối quan hệ giữa chúng.
*   *(Hình 2.13 Sơ đồ quan hệ thực thể (ERD) - Đính kèm hình ảnh)*

### 3.3. Thiết kế cơ sở dữ liệu

Cấu trúc chi tiết của các bảng trong cơ sở dữ liệu SQLite:

*   **Bảng `NhanVien` (Nhân Viên)**
    *   `ID` (INTEGER): Mã định danh duy nhất cho mỗi nhân viên (Khóa chính).
    *   `HoTen` (VARCHAR(45)): Họ và tên đầy đủ của nhân viên.
    *   `SDT` (VARCHAR(10)): Số điện thoại của nhân viên.
    *   `GioiTinh` (VARCHAR(10)): Giới tính nhân viên.
    *   `Username` (VARCHAR(45)): Tên đăng nhập của nhân viên (duy nhất).
    *   `Email` (VARCHAR(45)): Email của nhân viên.
    *   `Password` (VARCHAR(45)): Mật khẩu của nhân viên (cần mã hóa an toàn).

*   **Bảng `KhachHang` (Khách Hàng)**
    *   `ID` (INTEGER): Mã định danh duy nhất cho mỗi khách hàng (Khóa chính).
    *   `Ten` (VARCHAR(45)): Tên của khách hàng.
    *   `Ho` (VARCHAR(45)): Họ của khách hàng.
    *   `GioiTinh` (VARCHAR(45)): Giới tính của khách hàng.
    *   `MaBuuDien` (VARCHAR(45)): Mã bưu điện.
    *   `SDT` (VARCHAR(45)): Số điện thoại của khách hàng (duy nhất).
    *   `Email` (VARCHAR(45)): Địa chỉ email của khách hàng (duy nhất).
    *   `QuocTich` (VARCHAR(45)): Quốc tịch khách hàng.
    *   `CCCD` (INTEGER): Số Căn Cước Công Dân của khách hàng (duy nhất).
    *   `DiaChi` (VARCHAR(45)): Địa chỉ của khách hàng.

*   **Bảng `Phong` (Phòng)**
    *   `ID` (INTEGER): Mã định danh duy nhất cho mỗi phòng (Khóa chính).
    *   `LoaiPhong` (VARCHAR(100)): Loại phòng (ví dụ: Đơn, Đôi, VIP).
    *   `GiaTien` (FLOAT): Giá tiền một đêm cho phòng.
    *   `SoPhong` (INTEGER): Số phòng (duy nhất).
    *   `TrangThai` (VARCHAR(100)): Trạng thái phòng (Trống, Đang sử dụng, Đã đặt).

*   **Bảng `DatPhong` (Đặt Phòng)**
    *   `ID` (INTEGER): Mã định danh duy nhất cho mỗi lượt đặt phòng (Khóa chính).
    *   `MaKH` (INTEGER): Mã khách hàng (Khóa ngoại liên kết với `KhachHang.ID`).
    *   `MaPhong` (INTEGER): Mã phòng (Khóa ngoại liên kết với `Phong.ID`).
    *   `MaNV` (INTEGER): Mã nhân viên (Khóa ngoại liên kết với `NhanVien.ID`).
    *   `NgayNhanPhong` (DATE): Ngày nhận phòng.
    *   `NgayTraPhong` (DATE): Ngày trả phòng.
    *   `TrangThai` (VARCHAR(100)): Trạng thái đặt phòng (Đang đặt, Đã nhận phòng, Đã hủy).

*   **Bảng `HoaDon` (Hóa Đơn)**
    *   `ID` (INTEGER): Mã định danh duy nhất cho mỗi hóa đơn (Khóa chính).
    *   `MaDatPhong` (INTEGER): Mã đặt phòng (Khóa ngoại liên kết với `DatPhong.ID`).
    *   `NgayLap` (DATE): Ngày lập hóa đơn.
    *   `TongTien` (FLOAT): Tổng tiền của hóa đơn.
    *   `TrangThai` (VARCHAR(100)): Trạng thái thanh toán (Chưa thanh toán, Đã thanh toán).

### 3.4. Biểu đồ lớp

Biểu đồ lớp mô tả cấu trúc tĩnh của hệ thống, bao gồm các lớp (class), thuộc tính (attribute), phương thức (method) và mối quan hệ giữa chúng.
*   *(Hình 2.14 Biểu đồ lớp - Đính kèm hình ảnh)*

## 4. Thiết kế giao diện

Các giao diện người dùng được thiết kế bằng Tkinter, đảm bảo sự đơn giản và thân thiện:

*   **Giao diện đăng nhập:** Chứa các trường `entry_username`, `entry_password` và `button_login`.
    *   *(Hình 2.14 Giao diện đăng nhập - Đính kèm hình ảnh)*
*   **Trang chủ:** Giao diện chính sau khi đăng nhập thành công.
    *   *(Hình 2.15 Giao diện trang chủ - Đính kèm hình ảnh)*
*   **Giao diện quản lý khách hàng:** Cho phép xem, thêm, sửa, xóa, tìm kiếm thông tin khách hàng.
    *   *(Hình 2.16 Giao diện quản lý khách hàng - Đính kèm hình ảnh)*
*   **Giao diện quản lý phòng:** Cho phép xem, thêm, sửa, xóa, tìm kiếm thông tin phòng.
    *   *(Hình 2.17 Giao diện quản lý phòng - Đính kèm hình ảnh)*
*   **Giao diện đặt phòng:** Hỗ trợ các thao tác đặt phòng.
    *   *(Hình 2.18 Giao diện đặt phòng - Đính kèm hình ảnh)*
*   **Giao diện quản lý nhân viên:** Cho phép xem, thêm, sửa, xóa, tìm kiếm thông tin nhân viên.
    *   *(Hình 2.19 Giao diện quản lý nhân viên - Đính kèm hình ảnh)*
*   **Giao diện trả phòng (hóa đơn):** Xử lý quy trình trả phòng và tạo hóa đơn.
    *   *(Hình 2.20 Giao diện trả phòng (hóa đơn) - Đính kèm hình ảnh)*
*   **Giao diện báo cáo:** Hiển thị các báo cáo về khách hàng, phòng và doanh thu.
    *   *(Hình 2.20 Giao diện báo cáo - Đính kèm hình ảnh)*

## 5. Kết quả thực nghiệm

Phần mềm đã được triển khai và thử nghiệm các chức năng chính, bao gồm:

*   **Quản lý khách hàng:**
    *   Hiển thị danh sách khách hàng.
    *   Chức năng thêm khách hàng với các trường thông tin chi tiết.
    *   Chức năng sửa thông tin khách hàng đã chọn.
    *   Chức năng xóa khách hàng với xác nhận.
    *   Chức năng tìm kiếm khách hàng theo số điện thoại hoặc mã khách hàng.
    *   *(Đính kèm hình ảnh minh họa quá trình thêm, sửa, xóa, tìm kiếm khách hàng)*

*   **Quản lý phòng:**
    *   Hiển thị danh sách phòng.
    *   Chức năng thêm phòng với ID, số phòng, loại phòng, hạng phòng.
    *   Chức năng sửa thông tin phòng đã chọn.
    *   Chức năng xóa phòng với xác nhận.
    *   Chức năng tìm kiếm phòng theo ID phòng.
    *   *(Đính kèm hình ảnh minh họa quá trình thêm, sửa, xóa, tìm kiếm phòng)*

*   **Quản lý nhân viên:**
    *   Chức năng thêm nhân viên với các thông tin liên quan.
    *   Chức năng sửa thông tin nhân viên.
    *   Chức năng xóa nhân viên với xác nhận.
    *   Chức năng tìm kiếm nhân viên theo ID.
    *   *(Đính kèm hình ảnh minh họa quá trình thêm, sửa, xóa, tìm kiếm nhân viên)*

*   **Đặt phòng:**
    *   Chức năng thêm đặt phòng với thông tin khách hàng, phòng, ngày nhận/trả.
    *   Chức năng sửa thông tin đặt phòng.
    *   Chức năng xóa đặt phòng với xác nhận.
    *   Chức năng tìm kiếm đặt phòng theo số điện thoại.
    *   *(Đính kèm hình ảnh minh họa quá trình thêm, sửa, xóa, tìm kiếm đặt phòng)*

*   **Trả phòng (Hóa đơn):**
    *   Chọn đặt phòng và tạo hóa đơn tự động tính toán tổng tiền.
    *   Thông báo trả phòng thành công và cập nhật danh sách đặt phòng.
    *   *(Đính kèm hình ảnh minh họa quá trình trả phòng)*

*   **Báo cáo:**
    *   Báo cáo khách hàng.
    *   Báo cáo phòng.
    *   *(Đính kèm hình ảnh minh họa các báo cáo)*

## 6. Kết luận

### 6.1. Những kết quả đạt được

Phần mềm quản lý phòng khách sạn đã hoàn thành các mục tiêu đề ra, đáp ứng được các yêu cầu cơ bản của một hệ thống quản lý hiện đại:

*   **Thiết kế hệ thống:** Các chức năng chính (quản lý khách hàng, phòng, nhân viên, đặt phòng, trả phòng, báo cáo) đã được phân tích kỹ lưỡng qua biểu đồ use case, tuần tự và phân rã. Cơ sở dữ liệu chặt chẽ (KhachHang, Phong, NhanVien, DatPhong, HoaDon) đảm bảo tính toàn vẹn.
*   **Giao diện người dùng:** Đơn giản, dễ sử dụng, thân thiện, với các chức năng phân chia rõ ràng. Thông báo lỗi và cảnh báo được hiển thị rõ ràng.
*   **Tính năng nổi bật:** Quản lý CRUD (Create, Read, Update, Delete) cho khách hàng, phòng, nhân viên. Hỗ trợ quy trình đặt/trả phòng, tính toán chi phí tự động. Cung cấp các báo cáo cơ bản về khách hàng, phòng và doanh thu.

### 6.2. Hạn chế và hướng phát triển

*   **Hạn chế:**
    *   Chưa tích hợp các tính năng nâng cao như quản lý dịch vụ đi kèm (ăn uống, spa, v.v.).
    *   Chưa tích hợp các phương thức thanh toán trực tuyến.

*   **Hướng phát triển:**
    *   Tích hợp quản lý dịch vụ: Bổ sung khả năng quản lý các dịch vụ khách sạn đi kèm và tính toán vào hóa đơn.
    *   Hỗ trợ đa ngôn ngữ: Giúp hệ thống tiếp cận nhiều đối tượng người dùng hơn.
    *   Tích hợp thanh toán trực tuyến: Kết nối với các cổng thanh toán phổ biến để nâng cao tiện ích.
    *   Mở rộng quản lý chi nhánh: Phát triển khả năng quản lý tập trung nhiều chi nhánh khách sạn.

Phần mềm này là nền tảng vững chắc để tiếp tục nghiên cứu và phát triển các ứng dụng công nghệ thông tin trong tương lai, góp phần vào sự phát triển của ngành dịch vụ lưu trú tại Việt Nam.

---
