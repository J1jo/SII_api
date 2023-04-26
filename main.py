from flask import Flask, request, jsonify
from uf import get_uf_value

app = Flask(__name__)

@app.route('/uf', methods=['GET'])
def get_uf():
    date = request.args.get('date')
    if date is None:
        return jsonify({'error': 'Debe ingresar una fecha.'}), 400
    
    try:
        result = get_uf_value(date)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
