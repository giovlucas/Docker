# Use a imagem oficial do Node.js como base
FROM node:14-alpine AS build

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo package.json e o arquivo package-lock.json (se existir)
COPY package*.json ./

# Instale as dependências do npm
RUN npm install

# Copie todos os arquivos do diretório atual para o diretório de trabalho no container
COPY . .

# Construa o aplicativo para produção
RUN npm run build

# Estágio de produção
FROM nginx:alpine

# Copie os arquivos de compilação do estágio de construção para a pasta de conteúdo do servidor nginx
COPY --from=build /app/build /usr/share/nginx/html

# Exponha a porta 80 para fora do container
EXPOSE 80

# Comando para iniciar o servidor nginx em segundo plano
CMD ["nginx", "-g", "daemon off;"]
