Python Lambda API Service
===

Scaffolding for a python lambda backed REST API service using serverless

# Setup

Run `bash setup_env.sh` to setup all the required dev packages

# Running Locally

```
serverless offline
```

# Run Tests

  * Lints the code against pep8 standards.
  * Runs Unit Tests
  * Displays the Coverage Report

```
bash run_tests.sh
```

# Deploy to AWS

Deploy to AWS

Requires Docker

You must set the following env variables:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`

```
serverless deploy --stage production --verbose
```

# Endpoints

## hello

A basic hello world handler.

```
handler source: src/handlers/hello.py
API path: /hello
path parameters: name
query paramters: salutation
```

### examples

```
request: /hello
response: 'Hello World'
```

```
request: /hello/bob
response: 'Hello bob'
```

```
request: /hello/bob?salutation=lo
response: 'lo bob'
```

## debug

Returns a whole slew of information about your session and request. This endpoint makes it easy to see what you have access to inside your handler functions

**YOU SHOULD REMOVE THIS ENDPOINT BEFORE GOING TO PRODUCTION!**

```
handler source: src/handlers/debug.py
API path: /debug
path parameters: *
query paramters: *
```

## 404

This handler is your catch all handler.

```
handler source: src/handlers/404.py
API path: /*
path parameters: *
query paramters: *
```

