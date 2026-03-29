import logging
from mobile_appReactNative.config import Config
from mobile_appReactNative.database import Database
from mobile_appReactNative.models.user import User
from mobile_appReactNative.services.user_service import UserService

def main():
    logging.basicConfig(level=logging.INFO)
    config = Config()
    database = Database(config.database_url)
    user_service = UserService(database)
    
    user = User(name="John Doe", email="john@example.com")
    user_service.create_user(user)
    
    users = user_service.get_users()
    for user in users:
        print(user.name)

if __name__ == "__main__":
    main()