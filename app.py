from flask import Flask, render_template as render, request, redirect, url_for
from config import Config
from models import db, Category, Book
from forms import CategoryForm, BookForm

app = Flask(__name__, static_folder="public", template_folder="views")

app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def index():
    books = Book.query.all()
    categories = Category.query.all()
    return render("index.html", books=books, categories=categories)


"""
    CATEGORY ROUTES
"""
@app.route('/category', methods=['GET', 'POST'])
def category():
    form = CategoryForm(request.form)
    if request.method == "POST":
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('index'))
    return render("category.html", form=form)


@app.route('/category/edit/<int:id>', methods=['GET', 'POST'])
def category_edit(id=0):
    form = CategoryForm(request.form)
    category = Category.query.get(id)
    if request.method == "POST":
        category.name = form.name.data

        db.session.commit()
        return redirect(url_for('index'))

    form.id.data = category.id
    form.name.data = category.name
    return render('category.html', form=form)

@app.route('/category/delete/<int:id>')
def category_delete(id=0):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()

    print("Item deleted")
    return redirect(url_for('index'))


"""
    BOOK ROUTES
"""
@app.route('/book', methods=['GET', 'POST'])
def book():
    form = BookForm(request.form)
    if request.method == "POST":
        book = Book(
            title=form.title.data,
            author=form.author.data,
            year=form.year.data,
            quantity=form.quantity.data,
            category_id=Category.query.filter(Category.name.ilike(form.category.data)).first().id
        )

        db.session.add(book)
        db.session.commit()

        return redirect(url_for('index'))
    return render('book.html', form=form)


@app.route('/book/edit/<int:id>', methods=['GET', 'POST'])
def book_edit(id=0):
    form = BookForm(request.form)
    book = Book.query.get(id)
    if request.method == "POST":
        book.title = form.title.data,
        book.author = form.author.data,
        book.year = form.year.data,
        book.quantity = form.quantity.data,
        book.category_id = Category.query.filter(Category.name.ilike(form.category.data)).first().id

        db.session.commit()
        return redirect(url_for('index'))

    form.title.data = book.title
    form.author.data = book.author
    form.year.data = book.year
    form.quantity.data = book.quantity
    form.category.data = book.category.name
    return render('book.html', form=form)

@app.route('/book/delete/<int:id>')
def book_delete(id=0):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(port=8000)

