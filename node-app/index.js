import fs from "fs";
import express from "express";
import { Base } from "deta";

const app = express();
const port = parseInt(process.env.PORT) || 8080;

app.use(express.json());

app.get("/", async (request, response) => {
  response.send(fs.readFileSync("./static/index.html", "utf8"));
});

app.get("/todos", async (request, response) => {
  // Connect to a Base for storing todo items.
  const todos_base = Base("todos");
  // Fetch all items from the Base.
  const todos = await todos_base.fetch();
  // Return the items as JSON.
  response.send(todos.items);
});

app.post("/todos", async (request, response) => {
  // Connect to a Base for storing todo items.
  const todos_base = Base("todos");
  // Get the item from the request body.
  const item = request.body;
  // Put the item into the Base.
  const resp = await todos_base.put(item);
  // Return the response as JSON.
  response.send(resp);
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
