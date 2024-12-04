import { createQueue } from "kue";

const queue = createQueue()

function namedNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

queue.process('push_notification_code', (job, done) => {
    namedNotification(job.data.phoneNumber, job.data.message)
})