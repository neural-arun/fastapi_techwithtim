from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield 




app = FastAPI(lifespan=lifespan)


text_posts = {
    1: {"title": "New Post", "content": "first cool post"},
    2: {"title": "AI Is Changing Everything", "content": "Artificial intelligence is transforming how we build software, solve problems, and create value."},
    3: {"title": "Keep Learning", "content": "Consistency beats intensity when it comes to mastering a new skill. Learn something every day."},
    4: {"title": "Build in Public", "content": "Share what you build, what you learn, and what goes wrong. Progress becomes more valuable when others can learn from it."},
    5: {"title": "Think in Systems", "content": "Don't just solve individual problems. Build systems that solve entire categories of problems repeatedly."},
    6: {"title": "The Power of Python", "content": "Python makes it easier to turn ideas into working software, from automation scripts to AI-powered applications."},
    7: {"title": "AI Agents", "content": "AI agents become useful when models can interact with tools, execute workflows, and produce measurable outcomes."},
    8: {"title": "Learning by Doing", "content": "Tutorials provide direction, but building real projects develops engineering judgment. Write code, break things, and debug."},
    9: {"title": "Healthcare Innovation", "content": "Technology can help healthcare professionals spend less time on repetitive administrative work and more time caring for patients."},
    10: {"title": "Small Steps, Big Results", "content": "You don't need to build something revolutionary today. Solve one meaningful problem, then improve the solution."},
    11: {"title": "The Future Belongs to Builders", "content": "In the age of AI, the advantage belongs to people who can identify real problems, orchestrate intelligent systems, and deliver results."}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_posts(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail= "go fish somewhere else!")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post


    #FastAPI have automatic data validation which means it is going to check what is going in. 

