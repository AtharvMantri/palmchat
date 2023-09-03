from flask import Flask, request, render_template
import google.generativeai as palm
from datetime import datetime

app = Flask(__name__)

# Set your PaLM API key here
palm.configure(api_key='AIzaSyAkbv4lemKTxx1pW2_4YzTEHYMB2DWRq4c')

# Default chat parameters
defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}


@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = []
    user_input = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        context = "You are an ai Language model developed by atharv mantri who is 12 years old and studies at medicaps international school in class 8th B and he build you and your name is palm chat 2 you were developed to make an alternative of ChatGPT"
        examples = []
        messages = [user_input]

        response = palm.chat(
            **defaults,
            context=context,
            examples=examples,
            messages=messages
        )
        ai_response = response.last

        # Replace '\n' with '<br>' in the AI response
        ai_response = ai_response.replace('\n', '<br>')

        response_text.append(('user', user_input, get_current_time()))
        response_text.append(('ai', ai_response, get_current_time()))

    return render_template('index.html', response_text=response_text, user_input=user_input)


def get_current_time():
    time = datetime.now()
    timedate = f"{amorpm(time)} | {month(time)} {time.day}"
    return timedate


def amorpm(time):
    if time.hour >= 12 and time.second >= 1:
        return str(time.hour - 12) + ":" + str(time.minute) + " PM"
    else:
        return str(time.hour) + ":" + str(time.minute) + " AM"


def month(time):
    if time.month == 1:
        return "Jan"

    elif time.month == 2:
        return "Feb"

    elif time.month == 3:
        return "Mar"

    elif time.month == 4:
        return "Apr"

    elif time.month == 5:
        return "May"

    elif time.month == 6:
        return "Jun"

    elif time.month == 7:
        return "Jul"

    elif time.month == 8:
        return "Aug"

    elif time.month == 9:
        return "Sep"

    elif time.month == 10:
        return "Oct"

    elif time.month == 11:
        return "Nov"

    elif time.month == 12:
        return "Dec"

    else:
        return "Unknown"


if __name__ == '__main__':
    app.run(debug=True)