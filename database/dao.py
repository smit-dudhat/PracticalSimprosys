from database.model import Category, Product
from database.config import session

class GenericDao():

    model = None
    # def __init__(self, model_class) -> None:
    #     self.model = model_class

    # def get(self):
    #     data = session.query(self.model).all()            
    #     return data
        
class ProductDao(GenericDao):

    model = Product

    def get(self,id):
        data = session.query(self.model).get(id)
        context_data = {'id':data.id,
                        'title':data.title, 
                        'description':data.description, 
                        'price':data.price,
                        'status':data.status,
                        'created_at':data.created_at,
                        'updated_at':data.updated_at}            
        return {'data':context_data}
    
    def getall(self):
        data = session.query(self.model).all()
        data_list = []
        for i in data:
            data_list.append({'id':data.id,
                        'title':data.title, 
                        'description':data.description, 
                        'price':data.price,
                        'status':data.status,
                        'created_at':data.created_at,
                        'updated_at':data.updated_at})
        return {'data':data_list}


productdao = ProductDao()