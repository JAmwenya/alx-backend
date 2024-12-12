import kue from "kue";

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
	job.progress(50);
	done();
}

queue.process("push_notification_code", 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
