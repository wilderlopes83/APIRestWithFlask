from flask import Flask
from flask import jsonify # <- `jsonify` instead of `json`

app = Flask(__name__)

devs = [
    {
        'name': 'Wilder Lopes',
        'lang': 'Python'
    },
    {
        'name': 'Pedro Lopes',
        'lang': 'Baby'
    },
    {
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

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()