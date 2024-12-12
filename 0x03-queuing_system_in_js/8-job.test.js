import kue from "kue";
import createPushNotificationsJobs from "./8-job";

describe("createPushNotificationsJobs", function () {
	it("should display error if jobs is not an array", function () {
		expect(() => createPushNotificationsJobs("invalid", queue)).to.throw(
			"Jobs is not an array"
		);
	});

	it("should create jobs in the queue", function (done) {
		const jobs = [
			{ phoneNumber: "4153518780", message: "Test message" },
			{ phoneNumber: "4153518781", message: "Test message" },
		];
		const queue = kue.createQueue();
		queue.testMode = true;

		createPushNotificationsJobs(jobs, queue);
		expect(queue.testMode.jobs.length).to.equal(2);
		done();
	});
});
