from flask import Flask, jsonify, request
from datetime import datetime, timezone, timedelta
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 
tz = timezone(timedelta(hours=7))
date = datetime.now(tz=tz)

@app.route('/calculate_tax', methods=['POST'])
def calculate_tax():
    if request.is_json:
        data = request.get_json()
        currency = data.get('currency')
        price = data.get('price')
        payment_date = data.get('payment_date')
        tax = "7%"
        if ((currency is not None) and (price is not None) and (payment_date is not None)):
            total_price = price * 1.07
            response_data = {
                "currency": currency,
                "price": price,
                "tax": tax,
                "total_price": round(total_price, 2),
                "payment_date": payment_date,
                "date_after_tax": date.ctime()
            }
        else:
            return jsonify({"message": "Invalid input data"}), 400
        return jsonify({"message": "Tax calculated successfully", "data": response_data}), 200
    else:
        return jsonify({"message": "Invalid JSON format"}), 400


if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0',port =5000)
