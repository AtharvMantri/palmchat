# Palm 2 Chat - A Flask-Based Chat Application

Palm 2 Chat is a simple chat application built using Flask and powered by Google's PaLM 2 language model. It allows users to have conversations with an AI chatbot and receive responses in real-time. This chatbot can provide information, answer questions, and engage in a wide range of conversations.

## Features

- Real-time chat with a powerful AI chatbot.
- User-friendly interface with suggested messages.
- Conversations are displayed with timestamps.
- The AI responses can include HTML rendering (line breaks as `<br>` tags).
- Easy integration with the PaLM 2 language model.

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x
- Flask
- PaLM 2 API Key (You can obtain this from Google)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/AtharvMantri/palmchat.git
   ```
Install the required Python packages:

## Getting Started

To get started with Palm 2 Chat, follow these steps:

### 1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### 2. Set your PaLM 2 API key in the Flask app by modifying the palm.configure(api_key='YOUR_API_KEY_HERE') line in app.py.
### 3. Run the Flask application:

   ```bash
   python app.py
   ```
### 4. Open a web browser and navigate to http://localhost:5000 to start using the chat application.

### Usage
Enter your message in the input box and click "Send."
The chatbot will provide responses in real-time.
You can also click on suggested messages to populate the input box with them.

### Customization
You can customize this chat application by modifying the HTML and CSS in the templates/index.html file. You can also adjust the chatbot's behavior by configuring the defaults dictionary in app.py.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Flask - The web framework used.
Google's PaLM 2 - The AI language model.
Bootstrap - Used for styling.
Font Awesome - Used for icons.

### Author
Atharv Mantri
