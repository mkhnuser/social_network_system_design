from fastapi import FastAPI


app = FastAPI()


@app.get("/api/v1/posts/{id}", summary="Get post by id.")
async def get_post(id: int):
    """Get post by id."""
    return {"message": "Hello World"}


@app.post("/api/v1/posts", summary="Create post.")
async def create_post(id: int):
    """Create post."""
    return {"message": "Hello World"}


@app.delete("/api/v1/posts", summary="Delete post.")
async def delete_post(id: int):
    """Delete post."""
    return {"message": "Hello World"}


@app.put("/api/v1/posts/{id}", summary="Update post.")
async def update_post(id: int):
    """Update post"""
    return {"message": "Hello World"}


@app.get(
    "/api/v1/posts/{id}/comments",
    summary="Get comments which pertain to the post.",
)
async def get_post_comments(id: int):
    "Get comments which pertain to the post."
    return {"message": "Hello World"}


@app.get(
    "/api/v1/subscriptions/{id}",
    summary="Get subscriptions of a user with id `id`.",
)
async def get_user_subscriptions(id: int):
    "Get subscriptions of a user with id `id`."
    return {"message": "Hello World"}


@app.post(
    "/api/v1/subscriptions/{from_id}/{to_id}",
    summary="Subscribe a user `from_id` to a user `to_id`.",
)
async def create_subscription(from_id: int, to_id: int):
    "Subscribe a user `from_id` to a user `to_id`."
    return {"message": "Hello World"}


@app.delete(
    "/api/v1/subscriptions/{from_id}/{to_id}",
    summary="Unsubscribe a user `from_id` from a user `to_id`.",
)
async def delete_subscription(from_id: int, to_id: int):
    "Unsubscribe a user `from_id` from a user `to_id`."
    return {"message": "Hello World"}


@app.get(
    "/api/v1/places/",
    summary="Get top `k` popular places based on the number of mentions in posts.",
)
async def get_top_k_popular_places(k: int):
    "Get top `k` popular places based on the number of mentions in posts."
    return {"message": "Hello World"}


@app.get(
    "/api/v1/places/{place_id}/posts",
    summary="Get top `k` popular posts based on the `place_id`.",
)
async def get_top_k_popular_places(place_id: int, k: int):
    "Get top `k` popular places based on the number of mentions in posts."
    return {"message": "Hello World"}


@app.get(
    "/api/v1/feed/me",
    summary="Create feed for a particular user.",
)
async def create_feed_for_user():
    "Create feed for a particular user."
    return {"message": "Hello World"}


@app.get(
    "/api/v1/feed/{user_id}",
    summary="Get feed (posts) of a particular user.",
)
async def get_feed_based_on_user(user_id: int):
    "Get feed (posts) of a particular user."
    return {"message": "Hello World"}
