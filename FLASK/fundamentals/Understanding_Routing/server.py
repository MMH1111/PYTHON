from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#1. localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# localhost:5000/success - have it say "success"    
@app.route('/success')
def success():
  return "success"
    
    # app.run(debug=True) should be the very last statement! 

#2. localhost:5000/dojo - have it say "Dojo!"    
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'  # Return the string 'Dojo' as a response

#3. Create one url pattern and function that can handle the following examples:
# Example: localhost:5000/say/flask - have it say "Hi Flask!"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi, " + name + "!"

#4. Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35): 
# Example: localhost:5000/repeat/35/hello - have it say "hello" 35 times 
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''
    for i in range(0, num):
        output += f"<p>{word}</p>"
    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

