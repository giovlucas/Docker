# Use a imagem oficial do MySQL como base
FROM mysql:latest

# Configurações de ambiente para o MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=test_db
ENV MYSQL_USER=test_user
ENV MYSQL_PASSWORD=test_password

# Copiar o script SQL para inicializar o banco de dados
COPY init.sql /docker-entrypoint-initdb.d/

# Expor a porta padrão do MySQL (opcional)
EXPOSE 3306
