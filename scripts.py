import subprocess
import os

def create_user(username, password):
    try:
        subprocess.run(["net", "user", username, password, "/add"], check=True)
        print(f" User '{username}' created successfully.")

        subprocess.run(["net", "localgroup", "Users", username, "/add"], check=True)
        print(f" '{username}' added to 'Users' group.")

        subprocess.run(["net", "localgroup", "Administrators", username, "/delete"], check=False)  
    
    except subprocess.CalledProcessError as e:
        print(f" Error occurred: {e}")

# Example usage
create_user("testuser", "P@ssw0rd123")