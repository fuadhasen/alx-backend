// const redis = require('redis')
import redis from 'redis'

const client  = redis.createClient()


client.on('ready', () => {
    console.log('Redis client connected to the server')
})

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})


client.subscribe('holberton school channel')

// when it revieve message from publisher in this channel
client.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe()
        client.quit()
    }
    console.log(message)
})