import sqlite3
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from typing import List, Sequence

# from cyclopts import App, Parameter, validators
# from langchain_core.messages import AIMessage, BaseMessage
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_ollama import ChatOllama
# from langgraph.checkpoint.memory import MemorySaver
# from langgraph.graph import START, StateGraph
# from langgraph.graph.message import add_messages
# from rich.console import Console
# from typing_extensions import Annotated, TypedDict

connection = sqlite3.connect("./data/app-reviews.db")
df = pd.read_sql_query("SELECT * FROM bodyfat", connection)
df.shape



# DB_PATH = Path("./data/app-reviews.db")
# MODEL_NAME = "qwen2.5:14b"
# APP_CONFIG = {"configurable": {"thread_id": "42"}}


# @dataclass
# class Review:
#     package_name: str
#     text: str
#     rating: int


# class AppState(TypedDict):
#     messages: Annotated[Sequence[BaseMessage], add_messages]
#     reviews: str


# llm = ChatOllama(model=MODEL_NAME, temperature=0, keep_alive=-1)
# app = App(name="Revuvo", help="Analyze mobile app reviews")


# SYSTEM_PROMPT = """
# You're mobile app review analyzer. You'll be given reviews and answer questions about them.
# You always try to be helpful, accurate and brief.

# Here are the reviews:
# <reviews>
# {reviews}
# </reviews>
# """

# prompt_template = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             SYSTEM_PROMPT,
#         ),
#         MessagesPlaceholder(variable_name="messages"),
#     ]
# )


# def fetch_reviews(
#     min_rating: int,
#     max_rating: int,
#     max_reviews: int = 10,
# ) -> List[Review]:
#     with sqlite3.connect(DB_PATH) as conn:
#         cursor = conn.cursor()
#         cursor.execute(
#             """
#             SELECT package_name, review, rating
#             FROM reviews 
#             WHERE rating >= ?
#             AND rating <= ?
#             AND review IS NOT NULL
#             LIMIT ?
# """,
#             (min_rating, max_rating, max_reviews),
#         )
#         return [
#             Review(package_name=package_name, text=review, rating=rating)
#             for (package_name, review, rating) in cursor.fetchall()
#         ]


# def format_review(review: Review) -> str:
#     return f"""
# <review>
#     <text>{review.text}</text>
#     <rating>{review.rating}</rating>
# </review>
# """.strip()


# def call_model(state: AppState):
#     messages = prompt_template.invoke(state)
#     response = llm.invoke(messages)
#     return {"messages": response}


# def create_chat_app():
#     workflow = StateGraph(state_schema=AppState)
#     workflow.add_edge(START, "model")
#     workflow.add_node("model", call_model)
#     return workflow.compile(checkpointer=MemorySaver())


# @app.default
# def main(
#     min_rating: Annotated[
#         int, Parameter(validator=validators.Number(gte=1, lte=5))
#     ] = 1,
#     max_rating: Annotated[
#         int, Parameter(validator=validators.Number(gte=1, lte=5))
#     ] = 5,
#     max_reviews: Annotated[
#         int, Parameter(validator=validators.Number(gte=1, lte=30))
#     ] = 30,
# ):
#     """Analyze mobile app reviews.

#     Parameters
#     ----------
#     min_rating: int
#         Minimum rating of the review. Must be between 1 and 5.
#     max_rating: int
#         Maximum rating of the review. Must be between 1 and 5.
#     max_reviews: int
#         Maximum number of reviews to fetch. Default is 30.
#     """

#     reviews = fetch_reviews(min_rating, max_rating, max_reviews)
#     console = Console()
#     console.print(
#         f"""
# [b]Welcome to Revuvo![/b]

# Analyzing {len(reviews)} reviews with ratings between {min_rating} and {max_rating}.
#     """.strip()
#         + "\n"
#     )
#     reviews_text = "\n".join([format_review(review) for review in reviews])

#     chat_app = create_chat_app()
#     while True:
#         user_message = console.input("[i]You[/i]: ")
#         for chunk, _ in chat_app.stream(
#             {"messages": [user_message], "reviews": reviews_text},
#             APP_CONFIG,
#             stream_mode="messages",
#         ):
#             if isinstance(chunk, AIMessage):
#                 print(chunk.content, end="", flush=True)
#         print("\n")


if __name__ == "__main__":
    app()