import redis from "redis";

const client = redis.createClient();

client.on("connect", function () {
	console.log("Redis client connected to the server");
});

client.on("error", function (err) {
	console.log("Redis client not connected to the server:", err);
});

const cities = {
	Portland: 50,
	Seattle: 80,
	"New York": 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2,
};

Object.entries(cities).forEach(([city, population]) => {
	client.hset("ALX", city, population, redis.print);
});

client.hgetall("ALX", (err, reply) => {
	if (err) throw err;
	console.log(reply);
});
