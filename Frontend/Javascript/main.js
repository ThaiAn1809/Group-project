import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send('Started server');
})

app.listen(port, () => {
    console.log(`Successfully started server on port ${port}.`);
});