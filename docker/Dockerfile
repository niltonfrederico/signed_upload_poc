FROM python:3.9.7-slim-bullseye

WORKDIR /app

# Creates an appuser and change the ownership of the application's folder
RUN useradd appuser \
    && chown appuser /app

# Installs poetry and pip
RUN pip install --upgrade pip && \
    pip install poetry

# Copy dependency definition to cache
COPY --chown=appuser poetry.lock* pyproject.toml* /app/

# Installs projects dependencies as a separate layer
RUN poetry export -f requirements.txt -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install --require-hashes -r requirements.txt

COPY --chown=appuser . /app

EXPOSE 3000

# Switching to the non-root appuser for security
USER appuser
