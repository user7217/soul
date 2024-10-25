from flask import Flask, request, jsonify, render_template
from meta_ai_api import MetaAI  # Assuming this is the MetaAI library you're using

app = Flask(__name__, static_url_path='/assets')  # Custom path

# Initialize MetaAI object
ai = MetaAI()

@app.route('/')
def index():
    return render_template('index.html')  # The front-end (chat interface)

@app.route('/chat')
def chatbot():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.json.get('message')  # Get the user message from the POST request
    message1 = f"You are a mental health expert. Your job is to help people by sharing suggestions with respect to the questions they ask. Your answer or suggestions must be respectful and meaningful and related to improving mental health only. Make sure your answers are concise and never exceed 3 sentences. Answer the following question enclosed in three backticks: ```{user_input}```"    
    ai_response = ai.prompt(message1)  # Get the response from MetaAI
    print(ai_response.get('message'))  # Print the response to the console
    return jsonify({'response': ai_response.get("message")})  # Return the response to the frontend

if __name__ == '__main__':
    app.run(debug=True)
