from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))

def add_product(name, price, picture_link, description):
    product_object = Product(
        name=name,
        price=price,
        picture_link=picture_link,
    	description=description)
    session.add(product_object)
    session.commit()

add_product("mat", 230, "https://www.google.co.il/url?sa=i&source=images&cd=&ved=2ahUKEwiUyvj_m73mAhWrDmMBHVGIDw4QjRx6BAgBEAQ&url=https%3A%2F%2Fwww.indiamart.com%2Fproddetail%2Ffloor-yoga-mattress-13361710688.html&psig=AOvVaw1Msqjn5A0LhQWyCg8Ggp3P&ust=1576690510138890", "red, good mat")

def update_by_id(id, price, picture_link, description):
	product_object = session.query(
		Product).filter_by(
		id=id).first()
	product_object.price = price
	product_object.picture_link = picture_link
	product_object.description = description
	session.commit()


def delete_product(their_id):
	session.query(Product).filter_by(
		id=their_id).delete()
	session.commit()


def queery_all():
	products = session.query(
		Product).all()
	return products


def query_by_id(their_id):
	product = session.query(
       Product).filter_by(
       id=their_id).first()
	return product

def Add_To_Cart(product_id):
    Cart_object = Cart(
    	product_id=product_id)
    session.add(cart_object)
    session.commit()   
