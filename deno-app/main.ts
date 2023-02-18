import { serve } from "https://deno.land/std@0.173.0/http/server.ts";
import { Deta } from "https://esm.sh/deta@1.1.0";

const deta = Deta(Deno.env.get("DETA_PROJECT_KEY")!);

const handler = async (request: Request): Promise<Response> => {
  const url = new URL(request.url);
  switch (url.pathname) {
    case "/": {
      // Serve a static HTML file
      const body = new TextDecoder().decode(Deno.readFileSync("./static/index.html"));
      return new Response(body, {
        status: 200,
        headers: { "Content-Type": "text/html" },
      });
    }

    case "/users": {
      // Connect to a Base for storing user data
      const users_base = deta.Base("users");
      if (request.method === "GET") {
        // Fetch all users
        const users = await users_base.fetch();
        // Return the users as JSON
        return new Response(JSON.stringify(users.items), {
          status: 200,
          headers: { "Content-Type": "application/json" },
        });
      } else if (request.method === "POST") {
        // Get the user data from the request body
        const user = await request.json();
        // Put the user into the Base
        const resp = await users_base.put(user);
        // Return the response as JSON
        return new Response(JSON.stringify(resp), {
          status: 201,
          headers: { "Content-Type": "application/json" },
        });
      } else {
        // If the request method is not GET or POST, return a 405 error
        return new Response("Method Not Allowed", { status: 405 });
      }
    }

    default:
      return new Response("Not Found", { status: 404 });
  }
};

await serve(handler, {
  port: +Deno.env.get("PORT")! || 8080,
});
