export default function handler(req, res) {
  // Extract the path the user visited from the query string
  const { path } = req.query;

  // Log the path to Vercel runtime logs
  console.log("Visited path:", path || "/");

  res.status(200).send(`Logged path: ${path || "/"}`);
}
