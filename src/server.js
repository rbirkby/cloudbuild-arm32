const express = require('express');
const app = express();

app.get('/', async (req, res) => {
  res.send('Bonjour Cloud Run!');
});

// listen on the port defined by the "PORT" environment variable, or 8080
const server = app.listen(process.env.PORT || 8080, () => {
  const host = server.address().address;
  const port = server.address().port;

  console.log(`Example listening at http://${host}:${port}`);
});