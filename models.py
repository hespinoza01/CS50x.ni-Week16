from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Model = db.Model
Column = db.Column


class Category(Model):
    __tablename__ = "Category"

    id = Column(db.Integer, primary_key=True)
    name = Column(db.Text, nullable=False)

    def __repr__(self):
        return "{}".format(self.name)


class Book(Model):
    __tablename__ = "Book"

    id = Column(db.Integer, primary_key=True)
    title = Column(db.Text, nullable=False)
    author = Column(db.Text, nullable=False)
    year = Column(db.Integer, nullable=False)
    quantity = Column(db.Integer, nullable=False)
    category_id = Column(db.Integer, db.ForeignKey("Category.id"), nullable=False)

    category = db.relationship("Category")

    def __repr__(self):
        return "<Book: {}-{}>".format(self.title, self.author)
