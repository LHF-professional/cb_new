from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/button1', methods=['POST'])
def button1():
    if request.method == 'POST':
        # Disable the button
        button_id = request.form['button_id']
        response = {'button_id': button_id}
        return jsonify(response)

@app.route('/button2', methods=['POST'])
def button2():
    if request.method == 'POST':
        # Disable the button
        button_id = request.form['button_id']
        response = {'button_id': button_id}

        # Run script
        time.sleep(5)

        # Display images
        image_urls = ['image1.jpg', 'image2.jpg', 'image3.jpg']
        return jsonify({'image_urls': image_urls})

@app.route('/button3', methods=['POST'])
def button3():
    if request.method == 'POST':
        # Disable the button
        button_id = request.form['button_id']
        response = {'button_id': button_id}

        # Run script
        time.sleep(5)

        # Display success message
        message = 'Button 3 executed successfully'
        return jsonify({'message': message})

@app.route('/button4', methods=['POST'])
def button4():
    if request.method == 'POST':
        # Disable the button
        button_id = request.form['button_id']
        response = {'button_id': button_id}

        # Run script
        time.sleep(5)

        # Display error message
        message = 'An error occurred while executing Button 4'
        return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
