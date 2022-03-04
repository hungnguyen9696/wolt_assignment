##Wolt Summer 2022 Engineering Internships
___
Welcome to my WoltApp backend assignment

Language used: Python

NOTE: I use python3 and pip3 in my local machine. You may use python and pip depend on what you have on your machine so those following commands can be different.

---
###Install Dependencies:
In the project directory you can run:

> pip3 install -r requirements.txt 


___
###Running the server:
In the project directory you can run:

> uvicorn main:app --reload

If this command is not working, run:
> pip3 install uvicorn

The server is running on port  http://127.0.0.1:8000 

API documentation can be found at http://127.0.0.1:8000/docs
___
###Testing
In the project directory you can run:

> python3 test.py -v

Otherwise you can use Postman to test API requests. Choose POST method, http://127.0.0.1:8000/fee as the URI. In the header section, put application/json as content-type and in the body section put these following json:

    {
        "cart_value": 1500,
        "delivery_distance": 4000,
        "number_of_items": 8,
        "time": "2022-01-28T18:59:59Z"
    }

Feel free to modify those values to test the API.

