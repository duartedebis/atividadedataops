import psycopg2
import time
from flask import Flask
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app, version='1.0', title='API Flask ',
            description='API para conectar e consultar dados no PostgreSQL',
            doc='/swagger')

ns = api.namespace('Operação Matemática', description='Operações de conexão com PostgreSQL')

def get_connection():
    conn = psycopg2.connect(
        host="db",
        dbname="postgres",
        user="postgres",
        password="senha123"
        )
    return conn

oper_model = ns.model('OperModel', {
    'num1': fields.Float(required=True, description='Primeiro número'),
    'num2': fields.Float(required=True, description='Segundo número'),
})

@ns.route('/soma')
class Soma(Resource):
    @ns.expect(oper_model)
    @ns.response(200, 'Sucesso')
    def post(self):
        """
        Recebe num1 e num2 e retorna a soma
        """
        data = request.get_json()
        resultado = data['num1'] + data['num2']
        return {'resultado': resultado}, 200

@ns.route('/multiplicacao')
class Multiplicacao(Resource):
    @ns.expect(oper_model)
    @ns.response(200, 'Sucesso')
    def post(self):
        """
        Recebe num1 e num2 e retorna o produto
        """
        data = request.get_json()
        resultado = data['num1'] * data['num2']
        return {'resultado': resultado}, 200