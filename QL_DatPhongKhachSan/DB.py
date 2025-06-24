import sqlite3

def them_nhan_vien(ho_ten, so_dien_thoai, gioi_tinh, email, tai_khoan, mat_khau, db_path='quanlyphongkhachsan.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO nhanvien (ho_ten, so_dien_thoai, gioi_tinh, email, tai_khoan, mat_khau)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (ho_ten, so_dien_thoai, gioi_tinh, email, tai_khoan, mat_khau))

        conn.commit()
        print("Đã thêm nhân viên thành công.")

    except sqlite3.Error as e:
        print(f"Lỗi SQLite: {e}")

    finally:
        if 'conn' in locals() and conn:
            conn.close()