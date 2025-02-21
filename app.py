import threading
from reminders import start_reminder_scheduler
from flask import Flask, render_template, request
from command_handler import handle_command

app = Flask(__name__)

# Start the reminder scheduler in a separate thread
reminder_thread = threading.Thread(target=start_reminder_scheduler)
reminder_thread.daemon = True
reminder_thread.start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def web_command():
    user_command = request.form['command']
    handle_command(user_command)
    return "Command processed."

if __name__ == '__main__':
    app.run(debug=True)