// const redis = require('redis')
import redis from 'redis'
const { promisify } = require('util')

const client  = redis.createClient()
const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)


client.on('ready', () => {
    console.log('Redis client connected to the server')
})

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})


async function setNewSchool(schoolName, value) {
    const reply = await setAsync(schoolName, value)
    console.log(reply)
    
}

async function displaySchoolValue(schoolName) {
    const reply = await getAsync(schoolName)
    console.log(`Reply: ${reply}`)

}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');