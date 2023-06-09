# httpdatabase
JSON HTTP Database API: Easily create, modify, and delete key-value pairs using HTTP GET requests.

### ready to use instance
<a href=https://safeapi.itertools.repl.co target="_blank">https://safeapi.itertools.repl.co</a>

API provides a simple and intuitive way to interact with a JSON-based database using HTTP GET requests. With our API, anyone can easily create, modify, and delete key-value pairs in the database.

To create a new entry, simply send a GET request with the desired key-value pair as parameters, and our API will automatically add it to the database. To modify an existing entry, just send a GET request with the updated value, and our API will update the corresponding key-value pair. And if you need to remove an entry, just send a GET request with the key you want to delete, and our API will take care of the rest.

Our JSON HTTP Database API is designed to be user-friendly and accessible to all, making it easy for developers to interact with the database and perform CRUD (Create, Read, Update, Delete) operations seamlessly. Get started with our API now and experience the convenience and simplicity of managing your JSON database through HTTP GET requests.

### Host it yourself
1. Clone the repository to your local machine.
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Create a Firebase project and obtain the Firebase credentials (service account key) in JSON format.
4. Replace the fields in api/datamng.py with your base64 encoded Firebase JSON credentials and your Firebase realtime database url.
5. Run the Flask application
6. Open your web browser and go to http://localhost:5000 to access the web app.


### Usage
Availaible Routes -<br><br>

    /create - Creates a new key and assigns a value to it<br>
    i.e. /create?key=&value=<br>
    <br><br>
    /get - Gets the value of the provided key<br>
    i.e. /get?key=<br>
    <br><br>
    /update - Updates the key's value to the new value passed<br>
    i.e. /update?key=&value=<br>
    <br><br>
    /delete - Deletes a key from database<br>
    i.e. /delete?key=<br>
    
### Find Me on :
<p align="left">
  <a href="https://github.com/adhiraj-ranjan" target="_blank"><img src="https://img.shields.io/badge/Github-adhiraj--ranjan-green?style=for-the-badge&logo=github"></a>
  <a href="https://www.instagram.com/adhirajranjan_" target="_blank"><img src="https://img.shields.io/badge/IG-adhiraj_ranjan-pink?style=for-the-badge&logo=instagram"></a>
  <a href="https://t.me/adhirajranjan" target="_blank"><img src="https://img.shields.io/badge/TELEGRAM-ADHIRAJ%20RANJAN-blue?style=for-the-badge&logo=telegram"></a>
  
</p>
