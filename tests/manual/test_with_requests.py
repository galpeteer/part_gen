import requests

#Application needs to run for this test to work
# in CLI,from project root, run:
# uv run fastapi dev src/part_generator/main.py

response_washer = requests.post(
    "http://127.0.0.1:8000/v1/generate/washer",
    json={
        "outer_diameter": 20,
        "inner_diameter": 10,
        "thickness": 5
    }
)

with open("washer_manual_test.step", "wb") as f:
    f.write(response_washer.content)

response_bolt = requests.post(
    "http://127.0.0.1:8000/v1/generate/bolt",
    json={
        "diameter": 10,
        "length": 50
    }
)

with open("bolt_manual_test.step", "wb") as f:
    f.write(response_bolt.content)