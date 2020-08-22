from flask_calendar.authentication import Authentication
import config

authentication = Authentication(data_folder=config.USERS_DATA_FOLDER, password_salt=config.PASSWORD_SALT, failed_login_delay_base=0)

users = ["Antoine", "Maxime", "Adrien", "Anthony", "Aurelie", "Yoann", "Romain", "Thomas", "Michel", "Gilles", "Marie"]

for user in users:
    authentication.add_user(
        username=user,
        plaintext_password="LaBogerais",
        default_calendar="sample"
    )

# Delete a user
#authentication.delete_user(username="a username")