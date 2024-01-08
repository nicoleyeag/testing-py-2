from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    Game.query.delete()
    # adding a board game
    game = Game(name = 'Ticket to Ride', description = 'a cross-country train adventure')

    db.session.add(game)
    db.session.commit()

    # def setUp(self):					
    #     """Stuff to do before every test."""					
					
    # # Get the Flask test client					
    # self.client = app.test_client()					
    # app.config['TESTING'] = True					
					
    # # Connect to test database					
    # connect_to_db(app, "postgresql:///testdb")					
					
    # # Create tables and add sample data					
    # db.create_all()					
    # example_data()					














if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
