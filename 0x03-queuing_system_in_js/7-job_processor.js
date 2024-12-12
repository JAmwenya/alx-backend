import kue from "kue";

const queue = kue.createQueue();

const blacklistedNumbers = ["4153518780", "4153518781"];

function sendNotification(phoneNumber, message, job, done) {
	if (blacklistedNumbers.includes(phoneNumber)) {
		job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
		job.save();
		return done();
	}

	job.progress(50);
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
	done();
}

queue.process("push_notification_code_2", 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
