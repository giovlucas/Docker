-- Criar um banco de dados
CREATE DATABASE IF NOT EXISTS test_db;

-- Usar o banco de dados criado
USE test_db;

-- Criar uma tabela de exemplo
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);

-- Inserir dados de exemplo na tabela
INSERT INTO users (name, email) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com');
