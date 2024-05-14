from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form', methods=['GET', 'POST'])
def signup_form():
    if request.method == 'POST':
        username = request.form['username']
        # validate username
        validate_username_error = validate_username(username)
        if validate_username_error:  # Assuming this is your validation function
            # Pass the error message to the template
            return render_template('signup.html', validate_username_error=validate_username_error)
        else:
            # Proceed to thankyou page or handle the successful case
            return redirect(url_for('thankyou', username=username))
    # Initial page load or no error
    return render_template('signup.html', validate_username_error=None)

@app.route('/thankyou')
def thankyou():
    username = request.args.get('username')
    return render_template('thankyou.html', name=username)

def validate_username(username):
    '''
    Make sure a username meets the following requirements:
    # username must contain a lowercase letter.
    # username must contain an uppercase letter.
    # username must end with a number.
    
    if the username meets the requirements, return False.
    otherwise, return an error message stating which requirement the username does not meet. 
    '''
    # check if username contains a lowercase letter
    if not any(char.islower() for char in username):
        return 'Username must contain a lowercase letter.'
    # check if username contains an uppercase letter
    if not any(char.isupper() for char in username):
        return 'Username must contain an uppercase letter.'
    # check if username ends with a number
    if not username[-1].isdigit():
        return 'Username must end with a number.'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
