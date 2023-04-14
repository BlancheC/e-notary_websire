import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Replace the placeholders with your actual MySQL credentials
db_config = {
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "host": os.environ["DB_HOST"],
    "database": os.environ["DB_NAME"],
}

def get_connection():
    return mysql.connector.connect(**db_config)

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone VARCHAR(20) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            notary_id INT NOT NULL,
            appointment_type ENUM('individual', 'real_estate', 'legal') NOT NULL,
            appointment_time DATETIME NOT NULL,
            zoom_link VARCHAR(255) NOT NULL,
            UNIQUE(user_id, appointment_time),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (notary_id) REFERENCES notaries(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notaries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            appointment_id INT NOT NULL,
            stripe_payment_id VARCHAR(255) NOT NULL UNIQUE,
            amount DECIMAL(10, 2) NOT NULL,
            currency VARCHAR(3) NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (appointment_id) REFERENCES appointments(id)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables()
