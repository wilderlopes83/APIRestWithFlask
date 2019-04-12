from flask import Flask, jsonify, request


app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Wilder Lopes',
        'lang': 'Python'
    },
    {
        'id': 2,
        'name': 'Pedro Lopes',
        'lang': 'Baby'
    },
    {
        'id': 3,
        'name': 'Vanessa Lopes',
        'lang': 'Sharepoint'
    }
]

@app.route('/')
def home():
    return 'hello', 200

@app.route('/devs', methods=['GET'])
def getDevs():
    return jsonify(devs), 200        

@app.route('/devs/<string:lang>', methods=['GET'])
def getDevsPerLang(lang):
    #dois jeitos abaixo funcionam, mas com filter é mais elegante    
    devs_per_lang = list(filter(lambda x:x['lang']==lang, devs))    
    #devs_per_lang = [dev for dev in devs if dev['lang'] == lang]

    return jsonify(devs_per_lang), 200          

@app.route('/devs/<int:id>', methods=['GET'])
def getDevsPerId(id):
    
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    
    return jsonify({'error':'not found'}), 404

@app.route('/devs', methods=['POST'])    
def save_dev():
    data = request.get_json()
    devs.append(data)

    return jsonify(data), 201

@app.route('/devs/<int:id>', methods=['PUT'])    
def update_dev(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
        
            return jsonify(dev), 200
    
    return jsonify({'error': 'not found'}), 404

@app.route('/devs/<int:id>', methods=['DELETE'])    
def delete_dev(id):
    for i in range(len(devs)):
        if devs[i]['id'] == id:
            del devs[i]

            return jsonify({'message': 'Dev is no longer alive!'}), 200

    return jsonify({'error': 'not found'}), 404


if __name__ == '__main__':
    #app.run(debug=True)
    app.run()