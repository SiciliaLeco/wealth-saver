from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class TransactionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class TransactionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('transaction_type.id'), nullable=False)
    transaction_type = db.relationship('TransactionType', backref=db.backref('transactions', lazy=True))

    def __repr__(self):
        return f'<TransactionModel id={self.id} date={self.date} cost={self.cost} type={self.transaction_type.name}>'
    
