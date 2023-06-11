from flask import Flask, render_template, send_file, request
from urllib.request import urlopen

app = Flask(__name__)

# ################
# Welcome page
# ################
@app.route('/')
def main():
    return render_template('index.html')
  
# ################
# favicon
# ################
@app.route('/favicon.ico')
def favicon():
    return send_file("static/favicon.ico")

# ################
# SSRF
# ################

@app.route('/get')
def restservice():
    url = request.args.get('url')
    response = urlopen(url)
    return response.read()

# ################
# Main  
# ################
if __name__ == "__main__":
    
    app.logger.info("App is started ...")
    app.run(debug=False, host='0.0.0.0')
