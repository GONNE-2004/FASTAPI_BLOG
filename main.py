from fastapi import FastAPI
from fastapi.responses import HTMLResponse # Import the FastAPI class and HTMLResponse from the fastapi module

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False) # Define a GET endpoint at the root URL and access it with the home function
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) # Define a GET endpoint at /posts and access it with the home function
def home():
    return f"<h1>{posts[0]['title']}</h1>" # Return the title and content of the first post in the posts list as an HTML response


@app.get("/api/posts") # Define a GET endpoint at /api/posts and access it with the get_posts function
def get_posts():
    return posts