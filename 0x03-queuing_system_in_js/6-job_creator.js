import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const jobData = queue.create('push_notification_code', {
    phoneNumber: '1234567890',
    message: 'Account registered',
});

jobData
    .on('enqueue', () => {
        console.log(`Notification job created: ${jobData.id}`);
    })
    .on('complete', () => {
        console.log('Notification job completed');
    })
    .on('failed attempt', () => {
        console.log('Notification job failed');
    });
jobData.save();
