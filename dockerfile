FROM surnet/alpine-python-wkhtmltopdf as wkhtmltopdf

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