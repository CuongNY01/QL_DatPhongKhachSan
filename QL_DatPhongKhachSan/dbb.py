import sqlite3

def create_database(db_name="quanlyphongkhachsan.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            Ref INTEGER PRIMARY KEY,
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
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS details (
            Floor VARCHAR(45),
            RoomNo VARCHAR(45),
            RoomType VARCHAR(45),
            RoomClass VARCHAR(45)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doanhthu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roomavailable VARCHAR(45),
            contact VARCHAR(45),
            check_in DATETIME,
            check_out DATETIME,
            roomtype VARCHAR(45),
            roomclass VARCHAR(45),
            price_per_day DECIMAL(10, 2),
            num_of_days INTEGER,
            total_amount DECIMAL(10, 2)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nhanvien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ho_ten TEXT NOT NULL,
            so_dien_thoai TEXT,
            gioi_tinh TEXT,
            email TEXT,
            tai_khoan TEXT NOT NULL UNIQUE,
            mat_khau TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS room (
            Contact VARCHAR(45),
            check_in VARCHAR(45),
            check_out VARCHAR(45),
            roomtype VARCHAR(45),
            roomclass VARCHAR(45),
            roomavailable VARCHAR(45)
        )
    """)

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' and tables created successfully.")


def connect_to_database(db_name="quanlyphongkhachsan.db"):
    """Connects to the specified SQLite database."""
    try:
        conn = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def main():
    """Main function to create and connect to the database."""
    db_name = "hotel_management.db"  # Or any name you prefer
    create_database(db_name)
    conn = connect_to_database(db_name)

    if conn:
        # Example: Insert data into the customer table
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO customer (Ref, Name, Mother, Gender, PostCode, Mobile, Email, Nationality, Idproof, Idnumber, Address)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (1, "John Doe", "Jane Doe", "Male", "12345", "555-1234", "john.doe@example.com", "USA", "Passport", "AB123456", "123 Main St"))
            conn.commit()  # Save the changes
            print("Data inserted into customer table.")
        except sqlite3.Error as e:
            print(f"Error inserting data: {e}")


        conn.close()  # Close the connection when done
        print("Database connection closed.")
    else:
        print("Failed to connect to the database. Check the connection.")


if __name__ == "__main__":
    main()