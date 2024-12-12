import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

client.on("connect", function () {
	console.log("Redis client connected to the server");
});

client.on("error", function (err) {
	console.log("Redis client not connected to the server:", err);
});

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (err) {
		console.log(err);
	}
}

async function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

displaySchoolValue("ALX");
setNewSchool("ALXSanFrancisco", "100");
displaySchoolValue("ALXSanFrancisco");
