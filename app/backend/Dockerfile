# Use a imagem oficial do Node.js como base
FROM node:14-alpine

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos package.json e package-lock.json (se existir)
COPY package*.json ./

# Instale as dependências do npm
RUN npm install

# Copie todos os arquivos do diretório atual para o diretório de trabalho no container
COPY . .

# Exponha a porta em que o aplicativo é executado
EXPOSE 3000

# Comando para iniciar o aplicativo
CMD ["node", "index.js"]
