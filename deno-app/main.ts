import { serve } from "https://deno.land/std@0.173.0/http/server.ts";

const port = 8080;

const handler = (request: Request): Response => {
  if (request.method === "GET") {
    const body = new TextDecoder().decode(Deno.readFileSync("./static/index.html"));
    return new Response(body, {
      status: 200,
      headers: { "content-type": "text/html" },
    });
  }
  const naResp = new TextDecoder().decode(Deno.readFileSync("./static/405.html"));
  return new Response(
    naResp, {
      status: 405,
      headers: { "content-type": "text/html" },
    }
  );
};

await serve(handler, { port });
