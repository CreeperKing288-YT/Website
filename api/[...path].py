def handler(request, context):
    # For Vercel Python runtime, request.path gives the endpoint
    path = request.path.strip("/")
    print(f"Received request to endpoint: {path}")
    
    # Return response
    return {
        "statusCode": 200,
        "body": f"Endpoint received: {path}"
    }
