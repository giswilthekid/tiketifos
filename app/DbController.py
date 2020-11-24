from app.models import User, Tiket, DetailPembayaran
from app import response, app, db
from flask import request


#USER
#USER
#USER

def index():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def singleTransform(users):
    data = {
        'iduser': users.iduser,
        'name': users.name,
        'email': users.email,
        'sekolah': users.sekolah,
        'kota': users.kota
    }

    return data

def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array

def show(iduser):
    try:
        users = User.query.filter_by(iduser=iduser).first()
        if not users:
            return response.badRequest([], 'Empty....')

        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def adduser():
    try:
        name = request.json['name']
        email = request.json['email']
        sekolah = request.json['sekolah']
        kota = request.json['kota']
        password = request.json['password']

        users = User(name=name, email=email, sekolah=sekolah, kota=kota, password=password)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Berhasil membuat user!')

    except Exception as e:
        print(e)

def updateuser(iduser):
    try:
        name = request.json['name']
        email = request.json['email']
        sekolah = request.json['sekolah']
        kota = request.json['kota']
        password = request.json['password']

        user = User.query.filter_by(iduser=iduser).first()
        user.email = email
        user.name = name
        user.sekolah = sekolah
        user.kota = kota
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Berhasil update data user!')

    except Exception as e:
        print(e)

def deleteuser(iduser):
    try:
        user = User.query.filter_by(iduser=iduser).first()
        if not user:
            return response.badRequest([], 'Empty....')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Berhasil menghapus user!')
    except Exception as e:
        print(e)

#TIKET
#TIKET
#TIKET

def singleTransformTicket(ticket):
    data = {
        'idtiket': ticket.idtiket,
        'fullname' : ticket.fullname,
        'asalsekolah' : ticket.asalsekolah,
        'asalkota' : ticket.asalkota,
        'emailaktif' : ticket.emailaktif,
        'pilihanujian' : ticket.pilihanujian,
        'univtujuan' : ticket.univtujuan,
        'jurusan' : ticket.jurusan,
        'harga' : ticket.harga,
        'iduser': ticket.iduser
    }

    return data

def transformTicket(ticket):
    array = []
    for i in ticket:
        array.append(singleTransformTicket(i))
    return array

def indextiket():
    try:
        ticket = Tiket.query.all()
        data = transformTicket(ticket)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def showticket(idtiket):
    try:
        ticket = Tiket.query.filter_by(idtiket=idtiket).first()
        if not ticket:
            return response.badRequest([], 'Empty....')

        data = singleTransformTicket(ticket)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def showticketusers(iduser):
    try:
        ticket = Tiket.query.filter_by(iduser=iduser).all()
        if not ticket:
            return response.badRequest([], 'Empty....')

        data = transformTicket(ticket)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def buyticket(iduser):
    try:
        fullname = request.json['fullname']
        asalsekolah = request.json['asalsekolah']
        asalkota = request.json['asalkota']
        emailaktif = request.json['emailaktif']
        pilihanujian = request.json['pilihanujian']
        univtujuan = request.json['univtujuan']
        jurusan = request.json['jurusan']
        harga = request.json['harga']

        ticket = Tiket(fullname=fullname, asalsekolah=asalsekolah, asalkota=asalkota, emailaktif=emailaktif,
         pilihanujian=pilihanujian, univtujuan=univtujuan, jurusan=jurusan, harga=harga, iduser=iduser)
        db.session.add(ticket)
        db.session.commit()

        return response.ok('', 'Berhasil memesan tiket!')

    except Exception as e:
        print(e)

def updateticket(idtiket):
    try:
        fullname = request.json['fullname']
        asalsekolah = request.json['asalsekolah']
        asalkota = request.json['asalkota']
        emailaktif = request.json['emailaktif']
        pilihanujian = request.json['pilihanujian']
        univtujuan = request.json['univtujuan']
        jurusan = request.json['jurusan']
        harga = request.json['harga']

        ticket = Tiket.query.filter_by(idtiket=idtiket).first()
        ticket.fullname = fullname
        ticket.asalsekolah = asalsekolah
        ticket.asalkota = asalkota
        ticket.emailaktif = emailaktif
        ticket.pilihanujian = pilihanujian
        ticket.univtujuan = univtujuan
        ticket.jurusan = jurusan
        ticket.harga = harga

        db.session.commit()

        return response.ok('', 'Berhasil update data tiket!')

    except Exception as e:
        print(e)

def deleteticket(idtiket):
    try:
        ticket = Tiket.query.filter_by(idtiket=idtiket).first()
        if not ticket:
            return response.badRequest([], 'Empty....')

        db.session.delete(ticket)
        db.session.commit()

        return response.ok('', 'Berhasil menghapus tiket!')
    except Exception as e:
        print(e)

#PEMBAYARAN
#PEMBAYARAN
#PEMBAYARAN

def singleTransformPembayaran(pembayaran):
    data = {
        'idpembayaran': pembayaran.idpembayaran,
        'deskripsi': pembayaran.deskripsi,
        'bank': pembayaran.bank,
        'norek': pembayaran.norek,
    }

    return data

def transformPembayaran(pembayaran):
    array = []
    for i in pembayaran:
        array.append(singleTransformPembayaran(i))
    return array

def detailpembayaran():
    try:
        deskripsi = request.json['deskripsi']
        bank = request.json['bank']
        norek = request.json['norek']

        pembayaran = DetailPembayaran(deskripsi=deskripsi, bank=bank, norek=norek)
        db.session.add(pembayaran)
        db.session.commit()

        return response.ok('', 'Berhasil mengirim bukti pembayaran !')

    except Exception as e:
        print(e)

def updatepembayaran(idpembayaran):
    try:
        deskripsi = request.json['deskripsi']
        bank = request.json['bank']
        norek = request.json['norek']

        pembayaran = DetailPembayaran.query.filter_by(idpembayaran=idpembayaran).first()
        pembayaran.deskripsi = deskripsi
        pembayaran.bank = bank
        pembayaran.norek = norek

        db.session.commit()

        return response.ok('', 'Berhasil update data pembayaran!')

    except Exception as e:
        print(e)

def deletepembayaran(idpembayaran):
    try:
        pembayaran = DetailPembayaran.query.filter_by(idpembayaran=idpembayaran).first()
        if not pembayaran:
            return response.badRequest([], 'Empty....')

        db.session.delete(pembayaran)
        db.session.commit()

        return response.ok('', 'Berhasil menghapus pembayaran!')
    except Exception as e:
        print(e)

def indexpembayaran():
    try:
        pembayaran = DetailPembayaran.query.all()
        data = transformPembayaran(pembayaran)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def showpembayaran(idpembayaran):
    try:
        pembayaran = DetailPembayaran.query.filter_by(idpembayaran=idpembayaran).first()
        if not pembayaran:
            return response.badRequest([], 'Empty....')

        data = singleTransformPembayaran(pembayaran)
        return response.ok(data, "")
    except Exception as e:
        print(e)


#LOGIN
#LOGIN
#LOGIN

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Email yang dimasukkan salah !')

        if not user.checkPassword(password):
            return response.badRequest([], 'Password salah !')

        data = singleTransform(user)
        return response.ok(data, "Berhasil Login")
    except Exception as e:
        print(e)