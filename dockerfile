FROM surnet/alpine-wkhtmltopdf:3.16.2-0.12.6-full as wkhtmltopdf
FROM python:3.11-alpine as app

WORKDIR /home

# Setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

# Install pre-reqs
# wkhtmltopdf dependencies
RUN apk add --no-cache \
        libstdc++ \
        libx11 \
        libxrender \
        libxext \
        libssl1.1 \
        ca-certificates \
        fontconfig \
        freetype \
        ttf-droid \
        ttf-freefont \
        ttf-liberation \
        ;
# wkhtmltopdf copy bins from ext image
COPY --from=wkhtmltopdf /bin/wkhtmltopdf /bin/libwkhtmltox.so /bin/

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

# Create user and set ownership
RUN addgroup -S user && adduser -S user -G user && chown -R user:user .
USER user

ENTRYPOINT hypercorn src/app:app --bind 0.0.0.0:8001 -w 5