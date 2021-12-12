const db = require('./db')

setInterval(() => {
    temperatura = Math.round(Math.random() * (40 - 30) + 30)
    umidita = Math.round(Math.random() * (100 - 0) + 0)
    timestamp = new Date().getTime() 
    console.log(temperatura, umidita, timestamp);

    db.query(`INSERT INTO misure (temperatura, umidita, timestamp) VALUES (${temperatura}, ${umidita}, ${timestamp})`, (err, result) => {
        if (err) throw err
    });
}, 2000);