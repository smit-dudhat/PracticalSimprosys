from app_config import app
from flask.views import MethodView
from database.model import Category, Product
from database.dao import product
from database.config import session
from flask import render_template, request
from environ import TEMPLATE_DIR
# import uvicorn
from database import config

app.config['SQLALCHEMY_DATABASE_URI'] = config.db_url



@app.route("/")
def homeview():
    return render_template(f'index.html')

@app.route('/api/products',methods=['GET'])
def getproducts():
    products = session.query(Product).all()
    data = []
    for i in products:
        data.append({'id':i.id,'title':i.title,'description':i.description, 'price':i.price,'status':i.status, 'created_at':i.created_at,'updated_at':i.updated_at})

    return {'data':data},200

@app.route('/api/products/<int:id>', methods=['GET'])
def getproduct(id):
    product = session.query(Product).get(pk=id)
    data={'id':product.id,
          'title':product.title,
          'description':product.description, 
          'price':product.price,
          'status':product.status, 
          'created_at':product.created_at,
          'updated_at':product.updated_at}

    return {'data':data},200

@app.route('/api/products/',methods=['POST'])
def addproduct():
    data = request.get_json()
    product = Product(title=data.get('title'),
          description=data.get('description'),
          price=data.get('price'))
    session.add(product)
    session.commit()
    products = session.query(Product).all()
    data = []
    for i in products:
        data.append({'id':i.id,'title':i.title,'description':i.description, 'price':i.price,'status':i.status, 'created_at':i.created_at,'updated_at':i.updated_at})
    return {'data':data},201

@app.route('/api/products/<int:id>',methods=['DELETE'])
def removeproduct():
    product = session.query(Product).get(pk=id)
    session.delete(product)
    session.commit()
    return {'data':'Product has been removed'},203

@app.route('/api/products/<int:id>',methods=['PATCH'])
def updateproduct(id):
    data = request.get_json()
    product = product.get
    product.title = data.get('title')
    product.description = data.get('description')
    product.price = data.get('price')
    product.status = data.get('status')
    session.commit()
    product = session.query(Product).filter_by(id=id).first()
    data = {'id':product.id,'title':product.title,'description':product.description, 'price':product.price,'status':product.price, }
    return {'data':'Product has been removed'},203

if __name__ == "__main__":
    app.run(debug=True,host='localhost', port=3000)