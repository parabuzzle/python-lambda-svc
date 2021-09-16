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

```
bash run_tests.sh
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

