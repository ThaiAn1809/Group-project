import express from "express";
import bodyParser from "body-parser";

const app = express();
const port = 3000;

app.use(express.static("public"))

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
    res.render("homePage.ejs")
});

app.get("/pricing", (req, res) => {
    res.render("pricingPage.ejs")
})

app.get("/login", (req, res) => {
    res.render("loginAndRegisterPage.ejs")
})

app.get("/register", (req, res) => {
    res.render("loginAndRegisterPage.ejs")
})

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});