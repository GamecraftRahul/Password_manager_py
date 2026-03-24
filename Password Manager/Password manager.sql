-- Create Database
CREATE DATABASE IF NOT EXISTS password_manager;
USE password_manager;

-- Create Accounts Table
CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_type VARCHAR(50) NOT NULL,
    account_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(255) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample Data
INSERT INTO accounts (account_type, account_name, email, username, password, notes)
VALUES
('Email', 'Gmail', 'demo@gmail.com', 'demoUser', 'gmailPass123', 'Primary email account'),
('Social Media', 'Instagram', 'insta@mail.com', 'insta_user', 'instaPass2025', 'Main Insta account'),
('Banking', 'PayPal', 'paypal@mail.com', 'pp_user', 'PayPal!Secure123', 'Online transactions'),
('Gaming', 'Steam', 'steam@mail.com', 'steamKing', 'steamGame#45', 'Gaming account for Steam'),
('Cloud Storage', 'Dropbox', 'drop@mail.com', 'drop_admin', 'dropboxSecure!', 'File backup storage');
