CREATE DATABASE IF NOT EXISTS ai_shadow_mentor;
USE ai_shadow_mentor;
-- Tables are also auto-created by SQLAlchemy on first run (db.create_all()).
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  email VARCHAR(120) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS profiles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  target_role VARCHAR(80), skills TEXT, experience VARCHAR(30),
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS progress (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL, role VARCHAR(80), step_key VARCHAR(120),
  done TINYINT(1) DEFAULT 0,
  UNIQUE KEY uq_progress (user_id, role, step_key),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS chat_messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NULL, sender VARCHAR(10), message TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
