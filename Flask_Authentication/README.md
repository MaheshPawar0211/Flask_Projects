1) Install package flask-JWT.
2) Run the app.py file.
3) Create new endpoint to generate authentication token. 
----
    - POST http://127.0.0.1:5000/auth
    - Add below JSON into body
        {"username":"mahesh",
        "password":"asd"} 
    - Send request to application, application will return "access_token" as response.
    - Copy access token and add it to header for key= "Authorization".
     