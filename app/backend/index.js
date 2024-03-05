// index.js
const express = require('express');
const app = express();
const port = 3000;

// Rota básica
app.get('/', (req, res) => {
  res.send('Olá mundo! Este é o backend simples.');
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
