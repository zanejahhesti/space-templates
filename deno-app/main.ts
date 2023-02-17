import { serve } from "https://deno.land/std@0.173.0/http/server.ts";

const handler = (request: Request): Response => {
  if (request.method === "GET") {
    const body = new TextDecoder().decode(Deno.readFileSync("./static/index.html"));
    return new Response(body, {
      status: 200,
      headers: { "Content-Type": "text/html" },
    });
  }
  return new Response("Method Not Allowed", {
    status: 405,
  });
};

await serve(handler, {
  port: +Deno.env.get("PORT")! || 8080,
});
