from flask_restful import Resource, reqparse

serializador = reqparse.RequestParser()
serializador.add_argument(
    'actividadNombre',
    required = True,
    location = 'json',
    help='Falta el nombre de la actividad',
    type=str

)
class ActividadesController(Resource):
    def get(self):
        return {
            "message" : None,
            "content" : [{
                "actividadId":1,
                "actividadNombre":"Ir a la playa"
            },
            {
                "actividadId":2,
                "actividadNombre":"Cocinar"
            },{
                "actividadId":3,
                "actividadNombre":"Ir a cumpleaños"
            }]
        }, 201

    def post(self):
        data: dict = serializador.parse_args()
        #Lógica para BD
        actividadCreada = {
            "actividadId": 50,
            "actividadNombre": data.get('actividadNombre')
        }
        return{
            "message": "Actividad creada exitosamente",
            "content" : actividadCreada
        }, 201