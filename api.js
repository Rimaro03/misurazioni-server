const express = require('express');
const db = require('./db')
const cors = require('cors')

const app = express();
const PORT = 3002;
app.use(cors());
app.use(express.json())

// Route to get all posts
app.get("/misurazioni/db", (req, res) => {
    console.log(`DB: ${db}`);
    db.query("SELECT * FROM misure LIMIT 8", (err, result) => {
        if (err) {
            console.log(err)
        }
        res.send(result)
    });
});

app.get("/misurazioni/real", (req, res) => {
    let rilevazioni = {
        "temperatura": Math.floor(Math.random() * (40 - 10) + 10),
        "umidita": Math.floor(Math.random() * (100 - 10) + 10),
        "timestamp": new Date().getTime()
    }
    res.send(rilevazioni)
});

app.listen(PORT, () => {
    console.log(`Server is running on ${PORT}`)
});