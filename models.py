from website1 import db

class ResultTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text(), nullable=False)
    
    def __repr__(self):
        return '<ResultTable: {}>'.format(self.name)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.Text(), nullable=False)
    
    def __repr__(self):
        return '<Results: {}>'.format(self.name)
