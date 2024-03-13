from instapy import InstaPy
import schedule
import time

def job():
    try:
        # Replace 'your_instagram_username' and 'your_instagram_password' with your actual Instagram credentials
        session = InstaPy(username='your_instagram_username', password='your_instagram_password', headless_browser=True)

        # Start the session
        session.login()

        # Follow the target Instagram ID
        session.follow_by_id('target_instagram_id')

        # Add a congratulations message
        session.send_message('target_instagram_id', 'Congratulations! You have been followed by InstaPy.')

        # End the session
        session.end()

    except Exception as e:
        print(e)

# Schedule the job to run once a day at 6:35 AM and 4:22 PM
schedule.every().day.at("6:35").do(job)
schedule.every().day.at("16:22").do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)