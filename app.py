import pickle
from flask import Flask, request, jsonify

# Load your user-product matrix
user_item_matrix = pickle.load(open('user_item_matrix.pkl', 'rb'))

# Create the Flask app
app = Flask(__name__)

# Dummy recommendation logic
def recommend(user_id):
    if user_id not in user_product_matrix.index:
        return ["User not found"]
    # Example: return top 5 products not yet rated by this user
    user_row = user_product_matrix.loc[user_id]
    unrated_product = user_row[user_row.isna()].index.tolist()
    return unrated_products[:5]

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id'))
    result = recommend(user_id)
    return jsonify({'recommendations': result})

if __name__ == '__main__':
    app.run(debug=True)
