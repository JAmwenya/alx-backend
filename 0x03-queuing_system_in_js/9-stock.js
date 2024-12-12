import express from "express";
import redis from "redis";
import { promisify } from "util";

const app = express();
const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

const listProducts = [
	{ itemId: 1, itemName: "Suitcase 250", price: 50, stock: 4 },
	{ itemId: 2, itemName: "Suitcase 450", price: 100, stock: 10 },
	{ itemId: 3, itemName: "Suitcase 650", price: 350, stock: 2 },
	{ itemId: 4, itemName: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
	return listProducts.find((item) => item.itemId === id);
}

async function reserveStockById(itemId, stock) {
	await client.setAsync(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
	const stock = await getAsync(itemId);
	return stock || 0;
}

app.get("/list_products", (req, res) => {
	res.json(listProducts);
});

app.get("/list_products/:itemId", async (req, res) => {
	const item = getItemById(Number(req.params.itemId));
	if (!item) {
		return res.json({ status: "Product not found" });
	}
	const currentStock = await getCurrentReservedStockById(item.itemId);
	res.json({ ...item, currentQuantity: currentStock });
});

app.get("/reserve_product/:itemId", async (req, res) => {
	const item = getItemById(Number(req.params.itemId));
	if (!item) {
		return res.json({ status: "Product not found" });
	}
	const currentStock = await getCurrentReservedStockById(item.itemId);
	if (currentStock >= item.stock) {
		return res.json({
			status: "Not enough stock available",
			itemId: item.itemId,
		});
	}
	await reserveStockById(item.itemId, currentStock + 1);
	res.json({ status: "Reservation confirmed", itemId: item.itemId });
});

app.listen(1245, () => {
	console.log("Server running on port 1245");
});
