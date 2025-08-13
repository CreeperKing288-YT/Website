def handler(request):
    # Vercel passes a dict with 'query' and 'path'
    path = request.get("path", "")
    query = request.get("query", {})

    # Build full path with query string if it exists
    if query:
        qs = "&".join(f"{k}={v}" for k, v in query.items())
        full_path = f"{path}?{qs}"
    else:
        full_path = path

    # Log to Vercel console
    print(f"Received request to endpoint: {full_path}")

    # Return simple response
    return {
        "statusCode": 200,
        "body": f"Endpoint received: {full_path}"
    }
