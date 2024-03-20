# CHATin

CHATin is just a REST API server that acts as a bridge to connect to ChatGTP.

Once the server is running, the clients can connect to it using

        http://127.0.0.1:5000/chatin/api/v1.0/query

with a POST containing into the body a JSON with the only field 'message'.

For example, with a curl:

    curl -i -H "Content-Type: application/json" -X POST -d '{"message":"Tell something nice"}' http://127.0.0.1:5000/chatin/api/v1.0/query

There are some examples under src/samples in Python.


# Steps

## 1. Prepare everything

``pip install -r pre-req.txt''

## 2. To run

### Startup the REST server

``python src/server/chatgtp-api-server.py gmail-email gmail-password''

### Execute the example: generate cover letter for a job offer

# For a list of problems 
.... see ERRORS.md file


# The examples

To run the examples, set the PYTHONPATH to `src`, to let the samples search for client libraries.

    export PYTHONPATH=src

## Create Cover letter for a job position

The script `cover-letter.py` is a client to CHATin that creates a cover letter for a position.
It needs two files:

    1. `position.txt` : a text with the description of the position. Ideally without double line spaces
    2. `miniCV.txt`: a short list of your positions. Ideally without double line spaces

It needs three parameters: my name, company name, position name
For example:

    python src/samples/cover-letter.py "Gill Bates" "Minisoft" "CEO"

