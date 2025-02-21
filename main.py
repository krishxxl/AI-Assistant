import threading
from reminders import start_reminder_scheduler
from voice_recognition import listen_command
from command_handler import handle_command

def main():
    # Start the reminder scheduler in a separate thread
    reminder_thread = threading.Thread(target=start_reminder_scheduler)
    reminder_thread.daemon = True  # Daemonize thread to exit when the main program exits
    reminder_thread.start()

    while True:
        command = listen_command()
        if command:
            handle_command(command)

if __name__ == '__main__':
    main()