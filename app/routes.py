from app import app
from app import DbController
from flask import request


@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return DbController.index()
    else:
        return DbController.adduser()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return DbController.show(id)
    elif request.method == 'PUT':
        return DbController.updateuser(id)
    elif request.method == 'DELETE':
        return DbController.deleteuser(id)

@app.route('/ticket', methods=['GET'])
def ticket():
	return DbController.indextiket()

@app.route('/ticket/<id>', methods=['POST','PUT', 'GET', 'DELETE'])
def ticketDetail(id):
	if request.method == 'POST':
		return DbController.buyticket(id)
	elif request.method == 'GET':
		return DbController.showticket(id)
	elif request.method == 'PUT':
		return DbController.updateticket(id)
	elif request.method == 'DELETE':
		return DbController.deleteticket(id)

@app.route('/ticketuser/<id>', methods=['GET'])
def ticketuser(id):
	return DbController.showticketusers(id)

@app.route('/pembayaran', methods=['POST', 'GET'])
def pembayaran():
    if request.method == 'GET':
        return DbController.indexpembayaran()
    else:
        return DbController.detailpembayaran()

@app.route('/pembayaran/<id>', methods=['PUT', 'GET', 'DELETE'])
def pembayaranDetail(id):
    if request.method == 'GET':
        return DbController.showpembayaran(id)
    elif request.method == 'PUT':
        return DbController.updatepembayaran(id)
    elif request.method == 'DELETE':
        return DbController.deletepembayaran(id)

@app.route('/login', methods=['POST'])
def login():
    return DbController.login()