import abc
import model
import pickle
import os


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()

    
class PickleRepository(AbstractRepository):
       
       def __init__(self,path=None) -> None:
           self.path=path
           #create a dump of an empty list
          
           
           
           
       def add(self, batch):
           #open the dump, add the items at the end  uising + operator
           updated_items=[]
           with open(self.path, 'wb') as p:
               if  os.path.getsize(self.path) == 0:
                   pickle.dump(batch, p)
                   p.close()
                   updated_items.append(batch)
               else:
                    items = pickle.load(p)
                    updated_items=items.append(batch)
                    p.close()
           #delete the older pickle file and dump a new one with the new list in memory
           os.remove(self.path)
           with open(self.path, 'wb') as p1:
                pickle.dump(updated_items, p1)
                p1.close()

       def get(self, reference):
           with open(self.path, 'rb') as p:
               items = pickle.load(p)
               p.close()
               for e in items:
                  if e.reference==reference:
                     return e 
           
           return None

       def list(self):
           #read pickle file
           with open(self.path, 'rb') as p:
           #load list items
                 items=pickle.load(p)
                 #close file
                 p.close()
                 print(items)
                 return items
             
           
#p= PickleRepository("stock.pkl")
##print(len(p.list()))         
           
            
           

