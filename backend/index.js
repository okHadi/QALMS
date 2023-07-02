import express from 'express';
import cors from 'cors';
const app = express();
const port = 4306
import routes from './routes/routes.js';
// parse json request body
app.use(express.json());
// parse urlencoded request body
app.use(express.urlencoded({ extended: true }));

//api routes
app.use('/api', routes);

app.get('/api/test/', function (req, res) {
    res.json({ "message": "QALMS!" });
});

// TODO: Define CORS
app.listen(port, () => { console.log(`Node Server Started at Port ${port}`); })