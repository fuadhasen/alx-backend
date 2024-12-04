import {createClient, print} from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected connected to the server'));

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

function setHolbertonSchoolHash() {
    client.hset('HolbertonSchools', 'Portland', '50', print);
    client.hset('HolbertonSchools', 'Seattle', '80', print);
    client.hset('HolbertonSchools', 'New York', '20', print);
    client.hset('HolbertonSchools', 'Bogota', '20', print);
    client.hset('HolbertonSchools', 'Cali', '40', print);
    client.hset('HolbertonSchools', 'Paris', '2', print);
}

function displayHolbertonSchoolHash(schoolName) {
    client.hgetall('HolbertonSchools', (err, obj) => {
        if (err) {
            console.log(`Error: ${err}`);
        } else {
            console.log(obj);
        }
    });
}
setHolbertonSchoolHash();
displayHolbertonSchoolHash();
