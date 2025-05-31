# 1️⃣ Python 베이스 이미지
FROM python:3.12-slim

# 2️⃣ 작업 디렉토리 설정
WORKDIR /app

# 3️⃣ Poetry 설치
RUN pip install --no-cache-dir poetry==1.5.1

# 4️⃣ 프로젝트 파일 복사
# Ensure pyproject.toml and poetry.lock exist before copying
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# 5️⃣ 앱 코드 복사
COPY . .

# 6️⃣ 실행 포트 지정
EXPOSE 8080

# 7️⃣ Uvicorn 실행 (Poetry 환경에서)
CMD ["poetry", "run", "server", "--host", "0.0.0.0", "--port", "8080"]