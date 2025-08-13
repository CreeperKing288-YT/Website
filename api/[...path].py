from urllib.parse import unquote

def handler(request):
    # Get the path
    path = request.get("path", "")
    path = unquote(path)  # Decode URL-encoded paths

    # Get query string if it exists
    query = request.get("query", {})
    query_str = "&".join([f"{k}={v}" for k, v in query.items()])
    full_path = f"{path}?{query_str}" if query_str else path

    # Print to Vercel logs
    print(f"Received request to endpoint: {full_path}")

    # Return response
    return {
        "statusCode": 200,
        "body": f"Endpoint received: {full_path}"
    }
