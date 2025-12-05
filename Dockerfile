ARG NPM_REGISTRY=https://registry.npmmirror.com
ARG PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# Build frontend asset
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend

ARG NPM_REGISTRY
RUN npm config set registry ${NPM_REGISTRY}

COPY frontend/package*.json ./
RUN npm ci

COPY frontend .
RUN npm run build

# Final runtime image
FROM python:3.11-alpine AS runtime

ARG PIP_INDEX_URL

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FRONTEND_DIST_PATH=/app/frontend-dist \
    PIP_INDEX_URL=${PIP_INDEX_URL}

WORKDIR /app

RUN apk update \
    && apk add --no-cache build-base \
    && rm -rf /var/cache/apk/*

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./
COPY --from=frontend-builder /app/frontend/dist ./frontend-dist

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]