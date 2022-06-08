import model as m
import os


import repository as r

def test_add():
   path=os. getcwd()+"\\stock.pkl"
   b=m.Batch("100","1234x",450,eta=None)
   pckl=r.PickleRepository(path)
   pckl.add(b)
   #check if the item has been added by searching its reference
   item=pckl.get("100")
   
   assert b.__eq__(item) is True

def test_get():
   path=os. getcwd()+"\\stock.pkl"
   pckl=r.PickleRepository(path)
   # add five items and get any you want by there reference
   b1=m.Batch("600","2234x",550,eta=None)
   pckl.add(b1)
   b2=m.Batch("200","x234x",50,eta=None)
   pckl.add(b2)
   b3=m.Batch("300","2234x",40,eta=None)
   pckl.add(b3)
   b4=m.Batch("400","4234x",405,eta=None)
   pckl.add(b4)
   b5=m.Batch("500","3234x",540,eta=None)
   pckl.add(b5)
  
   #check if the item has been added by searching its reference
   item=pckl.get("500")
   
   assert b5.__eq__(item) is True

def test_list():
    #load the pickle file, and check if the file contains more than 5 items
    pt=os. getcwd()+"\\stock.pkl"
    p3=r.PickleRepository(pt)
    items=p3.list()
   # print(items)
    assert items is not None