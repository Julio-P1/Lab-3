import pymysql

class dbController:
    def __init__(self, hostIP, hostPort, hostPass, dbUser, dbName):

        #atributos
        self.host = hostIP
        self.port = hostPort
        self.username = dbUser
        self.db = dbName
        self.password = hostPass 
        #conexion a mysql
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.username,
            password=self.password,
            db=self.db
        )
        #ejecutar acciones - canal entre db y programa
        self.cursor = self.connection.cursor()
    

     #metodo para hacer un insert de nuevo usuario
    def insertNewUser(self, usName, usPass, email, now):
        sql = "INSERT INTO usuarios (username, password, email, creationDate) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (usName, usPass, email, now))
        self.connection.commit()
        self.dbCloseConnection()

    #metodo para modificar usuario, contraseña y correo
    def updateUser(self, usName, usPass, email, idU):
        sql = "UPDATE Usuarios SET username = %s, password = %s, email = %s WHERE idUsuario = %s"
        self.cursor.execute(sql, (usName, usPass, email, idU))
        self.connection.commit()
        self.dbCloseConnection()

    #obtener 1 usuario por su username
    def getUser(self, usName):
        sql = "SELECT * FROM Usuarios WHERE username = %s"
        self.cursor.execute(sql, usName)
        rows = self.cursor.fetchmany()
        self.dbCloseConnection()
        return rows

    #consultar informacion de compra
    def getCPurchase(self, usName):
        sql = "SELECT idCompra, username, fechaHoraCompra, CONVERT(totalCompra, CHAR) FROM Compras INNER JOIN Usuarios WHERE username = %s"
        self.cursor.execute(sql, usName)
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #consultar rango de fechas
    def getPurchaseRange(self, shopDate1, shopDate2):
        sql = "SELECT idCompra, fechaHoraCompra, CONVERT(totalCompra, CHAR) FROM Compras WHERE fechaHoraCompra BETWEEN %s AND %s"
        self.cursor.execute(sql, (shopDate1, shopDate2))
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows


    #Consultar compras que se encuentren en un rango especifico de total de compra
    def getRangeTotalPurchase(self, total1, total2):
        sql = "SELECT idCompra, fechaHoraCompra, CONVERT(totalCompra, CHAR) FROM Compras WHERE TotalCompra between %s and %s"
        self.cursor.execute(sql, (total1, total2))
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows

    #8. Consultar la lista de todos los productos y el precio de cada uno.
    def getAllProducts(self):
        self.cursor.execute("SELECT nombreProducto, CONVERT(precioUnitario, CHAR) FROM Productos")
        rows = self.cursor.fetchall()
        self.dbCloseConnection()
        return rows
    
    #editar el monto total de una compra
    def updateTotal(self, newTotal, totalCompra):
        sql = "UPDATE Compras SET totalCompra=%s WHERE idCompra = %s"
        self.cursor.execute(sql, (newTotal, totalCompra))
        self.connection.commit()
        self.dbCloseConnection()
    
    #10. Editar la cantidad y precio de un detalle de compra
    def updateQuantityNprice(self, newQuantity, newPrice, idDetails):
        sql = "UPDATE detalleCompras SET cantidad = %s, precio = %s WHERE idDetalleCompra = %s"
        self.cursor.execute(sql, (newQuantity, newPrice, idDetails))
        self.connection.commit()
        self.dbCloseConnection()
    
    #metoddo para cerrar la conexion a la base de datos
    def dbCloseConnection(self):
        self.connection.close()