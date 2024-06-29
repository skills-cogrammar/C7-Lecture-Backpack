const { MongoClient } = require('mongodb');
const winston = require('winston');
const { Console } = require('winston/lib/winston/transports');
require('winston-mongodb');

const log = winston.createLogger({
    level: 'info',
    transports: [
        new winston.transports.Console({format: winston.format.simple()})
    ],
});

log.info('Connecting to database...');

const url = "mongodb://localhost:27017/";

exports.logger = async (message) => {
    await doLogging(message);
}

async function doLogging(message){
    const client = new MongoClient(url);

    try{        
        await client.connect();

        const transportOptions = {
            db: await Promise.resolve(client.db('systemLogs')),
            options: {useUnifiedTopology: true},
            collection: 'log',
            leaveConnectionOpen: false
        }

        log.add(new winston.transports.MongoDB(transportOptions));


        log.info(message, {url})    
    } catch(err){
        console.log("well look whose failing now")
    }
    
}