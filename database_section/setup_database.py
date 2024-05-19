from app import db, Puppy, create_app

# Create an instance of the Flask application
app = create_app()

def setup_database(app):
    # Pushes an application context manually
    with app.app_context():
        # creates all the tables modelled in the app
        db.create_all()

        sam = Puppy('Sammy', 3)
        frank = Puppy('Frankie', 4)

        print(sam.id)  # Prints None, as the puppies are not yet committed to the database
        print(frank.id)  # Prints None

        db.session.add_all([sam, frank])
        db.session.commit()

        print(sam.id)  # Prints the id assigned to sam after committing
        print(frank.id)  # Prints the id assigned to frank

# Call the function with the Flask app instance
setup_database(app)