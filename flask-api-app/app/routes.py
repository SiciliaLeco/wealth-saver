from flask import Blueprint, jsonify, request
from app.models import db, TransactionModel, TransactionType, Debt, SavingGoal
from datetime import datetime
from flask import send_from_directory
api = Blueprint('api', __name__)


@api.route('/data/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Placeholder for item retrieval logic
    return jsonify({"item_id": item_id, "data": "sample item data"}), 200

@api.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = TransactionModel.query.all()
    result = [
        {
            "id": transaction.id,
            "date": transaction.date.strftime('%Y-%m-%d'),
            "cost": transaction.cost,
            "type": TransactionType.query.get(transaction.type_id).name
        }
        for transaction in transactions
    ]
    return jsonify(result), 200


@api.route('/debts', methods=['GET'])
def get_debts():
    debts = Debt.query.all()
    result = [
        {
            "id": debt.id,
            "amount": debt.amount,
            "description": debt.description,
            "date": debt.date.strftime('%Y-%m-%d')
        }
        for debt in debts
    ]
    return jsonify(result), 200
    
@api.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    t_type = TransactionType.query.filter_by(name=data['type']).first()
    if not t_type:
        t_type = TransactionType(name=data['type'])
        db.session.add(t_type)
        db.session.commit()
    transaction = TransactionModel(
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        cost=data['cost'],
        type_id=t_type.id
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added."}), 201

@api.route('/debts', methods=['POST'])
def add_debt():
    data = request.get_json()
    debt = Debt(
        amount=data['amount'],
        description=data.get('description', ''),
        date=datetime.strptime(data['date'], '%Y-%m-%d')
    )
    db.session.add(debt)
    db.session.commit()
    return jsonify({"message": "Debt added."}), 201


@api.route('/suggest-goal', methods=['GET'])
def suggest_goal():
    total_income = db.session.query(db.func.sum(TransactionModel.cost)).join(TransactionType).filter(TransactionType.name == 'income').scalar() or 0
    total_expense = db.session.query(db.func.sum(TransactionModel.cost)).join(TransactionType).filter(TransactionType.name == 'expense').scalar() or 0
    total_debt = db.session.query(db.func.sum(Debt.amount)).scalar() or 0
    net = total_income - total_expense - total_debt
    suggested = max(net * 0.1, 0)
    goal = SavingGoal(target_amount=suggested, suggested=True)
    db.session.add(goal)
    db.session.commit()
    return jsonify({"suggested_saving_goal": suggested})



@api.route('/frontend/<path:filename>')
def frontend_static(filename):
    return send_from_directory('../frontend', filename)