# Docsumo Backend Assignment

## Installation Steps

1. Create a virtual environment of name `.venv`
    ```
    python3 -m venv /path/to/new/virtual/environment
    ```
2. Activate the newly created virtual environment
    ```
    source /path/to/new/virtual/environment
    ```
3. Install requirements
   ```
   pip3 install -r requirements.txt 
   ```
4. Create and setup values in `.env` file.
5. Start development server
   ```
   flask run --port <port_number>
   ```
7. Start production server.  
   In your production environment, make sure the ``FLASK_DEBUG`` environment variable is
   unset or is set to ``0``
   ```
   gunicorn --workers=<number of workers here> docsumo.wsgi:app
   ```

## Endpoints
```
POST  /search/text/
Payload-  {“file_name”: "", “position”: [23, 34, 56, 100]}
Response- {"text": ""}
```

