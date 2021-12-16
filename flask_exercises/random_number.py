from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/random', methods = ["POST", "GET"])
def home():
   num = random.randint(0, 5)
   return str(num)
if __name__ == '__main__':
   app.run()

