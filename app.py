from controllers.actividades import ActividadesController
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api =Api(app)

# ====> R U T A S 
api.add_resource(ActividadesController, '/actividades')

print('Yo soy un cambio')

if __name__ == '__main__':
    app.run(debug=True)