from app import db, Puppy, create_app

# Create an instance of the Flask application
app = create_app()

def setup_database(app):
    # Pushes an application context manually
    with app.app_context():

        ## CREATE ##
        my_puppy = Puppy('Rufus', 5)
        db.session.add(my_puppy)
        db.session.commit()

        ## READ ##
        all_puppies = Puppy.query.all() # list of all puppies in the table
        print(all_puppies)

        # SELECT by ID
        puppy_one = Puppy.query.get(1)
        print(puppy_one)

        # FILTER
        puppy_frankie = Puppy.query.filter_by(name='Frankie')
        print(puppy_frankie.all())

        ## UPDATE ##
        first_puppy = Puppy.query.get(1)
        first_puppy.age = 10
        db.session.add(first_puppy)
        db.session.commit()

        ## DELETE ##
        second_puppy = Puppy.query.get(2)
        db.session.delete(second_puppy)
        db.session.commit()

        all_puppies = Puppy.query.all() # list of all puppies in the table
        print(all_puppies)
        
setup_database(app)