FROM python:3.11-alpine

WORKDIR /home

# Setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

# Install pre-reqs
# pdfkit
RUN apk install wkhtmltopdf

# Install tools
RUN apk add nano

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --deploy --system

# Install application
COPY . .
RUN chmod 0644 crontab

# Create user and set ownership
RUN addgroup -S user && adduser -S user -G user && chown -R user:user .
USER user

ENTRYPOINT hypercorn src/app:app --bind 0.0.0.0:8001