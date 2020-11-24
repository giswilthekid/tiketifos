from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sekolah = db.Column(db.String(120), nullable=False)
    kota = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    ticket = db.relationship('Tiket', backref='author', lazy=True)

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.email, self.sekolah, self.kota)

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)

class Tiket(db.Model):
    idtiket = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), nullable=False)
    asalsekolah = db.Column(db.String(20), nullable=False)
    asalkota = db.Column(db.String(20), nullable=False)
    emailaktif = db.Column(db.String(20), nullable=False)
    pilihanujian = db.Column(db.String(20), nullable=False)
    univtujuan = db.Column(db.String(20), nullable=False)
    jurusan = db.Column(db.String(20), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    iduser = db.Column(db.Integer, db.ForeignKey('user.iduser'), nullable=False)
    pembayaran = db.relationship('DetailPembayaran', backref='author', lazy=True)

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.fullname, self.asalsekolah, self.asalkota, self.emailaktif, self.pilihanujian,
         self.univtujuan, self.jurusan, self.harga)

class DetailPembayaran(db.Model):
    idpembayaran = db.Column(db.Integer, primary_key=True)
    deskripsi = db.Column(db.String(20))
    totalharga = db.Column(db.Integer, default=0)
    bank = db.Column(db.String(20))
    norek = db.Column(db.String(30))
    buktitransfer = db.Column(db.String(20), default='default.jpg')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idtiket = db.Column(db.Integer, db.ForeignKey('tiket.idtiket'))

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.deskripsi, self.totalharga, self.bank, self.norek, self.buktitransfer)