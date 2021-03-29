from flask import Flask, request, jsonify
import json
import collections
import hashlib
from datetime import datetime
import _datetime
import DBController as DBC

app = Flask(__name__)

#ruta princial
@app.route('/')
def saludo():
    return 'Laboratorio # 3'


#ruta para insertar nuevo usuario
@app.route('/newUser', methods=['POST'])
def createNewUser():
    try:
        data = request.get_json()
        print(data)
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')

        #encripcion del password
        usPass = hashlib.md5(data['password'].encode('utf-8'))
        usNameEncode = hashlib.md5(data['username'].encode('utf-8'))
        usPassEncode = (usNameEncode.hexdigest() + usPass.hexdigest()).encode('utf-8')
        ecriptedPass = (hashlib.md5(usPassEncode).hexdigest()).encode('utf-8')

        #email
        email = data['email'].encode('utf-8')
  

        #insertamos fecha con formato de SQL
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        dbConnection.insertNewUser(data['username'], ecriptedPass, email, now)
        return jsonify({'message: ': 'Nuevo usuario creado.'})
    except Exception as ex:
        print(ex)
        return jsonify({'message: ': 'Ocurrio un error.'})

#ruta para modificar usuario y contraseña
@app.route('/modify/<userId>', methods=['PUT'])
def modify_user_info(userId):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')

        #encripcion del password
        usPass = hashlib.md5(data['password'].encode('utf-8'))
        usNameEncode = hashlib.md5(data['username'].encode('utf-8'))
        usPassEncode = (usNameEncode.hexdigest() + usPass.hexdigest()).encode('utf-8')
        ecriptedPass = (hashlib.md5(usPassEncode).hexdigest()).encode('utf-8')

        #email
        email = data['email'].encode('utf-8')

        dbConnection.updateUser(data['username'], ecriptedPass, email, userId)
        return jsonify({'message: ': 'Informacion de usuario modificada.'})
    except Exception as ex:
        print(ex)
        return jsonify({'message: ': 'Ocurrio un error.'})

#3. Consultar la informacil usuario en particular en base a su username.
@app.route('/oneUser/<user>', methods=['GET'])
def get_one_user(user):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        salida = dbConnection.getUser(user)
        return jsonify(salida)
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error'})

#Consultar la informacion de la compra de un usuario en base a su username
@app.route('/onePurchase/<userNm>', methods=['GET'])
def get_one_purchase(userNm):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        salida1 = dbConnection.getCPurchase(userNm)
        return jsonify(salida1)
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error'})

@app.route('/shopRange/<date1>/<date2>', methods=['GET'])
def get_shop_rangeDate(date1, date2):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        resultado = dbConnection.getPurchaseRange(date1, date2)
        return jsonify(resultado)
    except Exception as ex:
        print(ex)

#Consultar compras que se encuentren en un rango especifico de valor 
@app.route('/rangeTotalPurchase/<TotalCompra>/<TotalCompra2>', methods=['GET'])
def get_reange_Total_purchase(TotalCompra, TotalCompra2):
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        salida3 = dbConnection.getRangeTotalPurchase(TotalCompra, TotalCompra2)
        return jsonify(salida3)
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error'})

#8. Consultar la lista de todos los productos y el precio de cada uno.
@app.route('/allProducts',  methods=['GET'])
def get_all_products():
    try:
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        salida4 = dbConnection.getAllProducts()
        return jsonify(salida4)
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error'})

#editar el monto total de una compra
@app.route('/SetNewTotal/<compraId>', methods=['PUT'])
def update_creation_Total(compraId):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        dbConnection.updateTotal(data['totalCompra'], compraId)
        return jsonify({'message': 'Total Actualizado Exitosamente.'})
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error.'})

#editar la cantidad y precio de detalle de Compra
@app.route('/setNewQuantityPrice/<detailID>', methods=['PUT'])
def update_quantity_price(detailID):
    try:
        data = request.get_json()
        dbConnection = DBC.dbController('127.0.0.1', 3306, '%servjul^%', 'root', 'onlineShop')
        dbConnection.updateQuantityNprice(data['newQuantity'], data['newPrice'], detailID)
        return jsonify({'message': 'Nueva cantidad y precio en detalle de compra.'})
    except Exception as ex:
        print(ex)
        return jsonify({'message': 'Ocurrio un error.'})


if(__name__ == '__main__'):
    app.run(debug=True)