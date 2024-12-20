import {createClient, print} from 'redis';
import promisify from 'util';

const client = createClient();

client.on('connect', () => console.log('Redis client connected connected to the server'));

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
    await client.get(schoolName, (err, value) => {
        if (err) {
            console.log(`Error: ${err}`);
        } else {
            console.log(value);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
