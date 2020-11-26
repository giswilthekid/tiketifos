from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(JSON)
    email = db.Column(JSON)
    sekolah = db.Column(JSON)
    kota = db.Column(JSON)
    password = db.Column(JSON)
    id_ticket = db.relationship('Tiket', backref='author', lazy=True)

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.email, self.sekolah, self.kota)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)

class Tiket(db.Model):
    idtiket = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(JSON)
    asalsekolah = db.Column(JSON)
    asalkota = db.Column(JSON)
    emailaktif = db.Column(JSON)
    pilihanujian = db.Column(JSON)
    univtujuan = db.Column(JSON)
    jurusan = db.Column(JSON)
    harga = db.Column(JSON)
    status = db.Column(db.Boolean, default=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    iduser = db.Column(db.Integer, db.ForeignKey('user.iduser'), nullable=False)
    pembayaran = db.relationship('DetailPembayaran', backref='author', lazy=True)

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.fullname, self.asalsekolah, self.asalkota, self.emailaktif, self.pilihanujian,
         self.univtujuan, self.jurusan, self.harga)

class DetailPembayaran(db.Model):
    idpembayaran = db.Column(db.Integer, primary_key=True)
    deskripsi = db.Column(JSON)
    totalharga = db.Column(db.Integer, default=0)
    bank = db.Column(JSON)
    norek = db.Column(JSON)
    buktitransfer = db.Column(db.String(20), default='default.jpg')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idtiket = db.Column(db.Integer, db.ForeignKey('tiket.idtiket'))

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.deskripsi, self.totalharga, self.bank, self.norek, self.buktitransfer)