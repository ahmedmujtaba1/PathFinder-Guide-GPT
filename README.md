# Path Guide GPT API

This API is designed to provide suggestions for travelers exploring new places. It uses a GPT model to generate recommendations on must-visit places and local dishes.

## Made by Ahmed Mujtaba

## Setup and Installation

To run this project, you need to have Python and the necessary packages installed. You can set up your environment with the following steps:

1. Clone the repository to your local machine.
2. Create a virtual environment:
    ``` python -m venv venv
3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```
4. Install the required packages:

 ``` pip install -r requirements.txt

## Running the API

Once you have set up your environment, you can start the API with the following command:

``` uvicorn main:app --reload


This will start the API server, and you can then send POST requests to the `/explore/` endpoint to get travel suggestions.
