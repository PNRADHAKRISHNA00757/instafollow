from instagram_private_api import Client

def follow_user(username):
    # Replace 'your_username' and 'your_password' with your Instagram credentials
    api = Client('your_username', 'your_password')

    # Get the user id by their username
    user_info = api.username_info(username)
    user_id = user_info['user']['pk']

    # Follow the user
    result = api.friendships_create(user_id)

    if result['status'] == 'ok':
        print(f"Successfully followed {username}")
    else:
        print(f"Failed to follow {username}")

# Replace 'target_username' with the username of the user you want to follow
follow_user('target_username')