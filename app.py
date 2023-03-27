from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    script_name = request.form['script']
    try:
        os.system(f'python scripts/{script_name}')
        success = True
    except:
        success = False
    if success:
        if script_name == 'script2.py':
            images = os.listdir('static/images')
            if images:
                return {'success': True, 'images': images}
            else:
                return {'success': True}
        else:
            return {'success': True}
    else:
        return {'success': False}

if __name__ == '__main__':
    app.run(debug=True)
