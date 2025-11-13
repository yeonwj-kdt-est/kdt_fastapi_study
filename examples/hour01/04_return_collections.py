from fastapi import FastAPI

# FastAPI 문서 페이지 경로를 /api/docs, 
# 스펙 JSON 경로를 /api/openapi.json으로 지정하는 설정.
app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

COURSE_TOPICS = ["fastapi-intro", "http-basics", "json", "uvicorn"]

def get_course_topics() -> dict:
    """강의 토픽을 리스트로 제공하고, 리스트 개수 카운트."""
    return {"topics": COURSE_TOPICS, "count": len(COURSE_TOPICS)}

@app.get("/course/topics")
def topics_endpoint() -> dict:
    return get_course_topics()

if __name__ == "__main__":
    # uvicorn --reload examples.hour01.04_return_collections:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)