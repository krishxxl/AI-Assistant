import schedule
import time
from text_to_speech import speak

# List to store reminders
reminders = []

def add_reminder(task, time_str):
    reminders.append({"task": task, "time": time_str})
    speak(f"Reminder added: {task} at {time_str}.")

def check_reminders():
    current_time = time.strftime("%H:%M")
    for reminder in reminders:
        if reminder["time"] == current_time:
            speak(f"Reminder: {reminder['task']}")
            reminders.remove(reminder)  # Remove the reminder after notifying

# Schedule the reminder checker to run every minute
schedule.every(1).minutes.do(check_reminders)

def start_reminder_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)