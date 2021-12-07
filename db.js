const mysql = require('mysql');

let db = mysql.createConnection({
    host: '192.168.1.114',
    user: 'admin',
    password: '7907',
    database: 'misurazioni'
});

db.connect((err) => {
    if (err) {
        console.log('Error connecting to Db');
        return;
    }
    console.log('Connection established');
});

module.exports = db;