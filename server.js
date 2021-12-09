const db = require('./db')

while (True) {
    temperatura = Math.random() * (40 - 30) + 30
    umidita = Math.random() * (100 - 0) + 0
    timestamp = new Date()

    db.query(`INSERT INTO misure (temperatura, umidita, timestamp) VALUES (${temperatura}, ${umidita}, ${timestamp})`, (err, result) => {
        if (err) throw err
    });

    sleep(5000)
}