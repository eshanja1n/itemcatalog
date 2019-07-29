from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from database_setup import Category, CatChar, User, Base

engine = create_engine('sqlite:///charcatalog.db')
# clears database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# create dummy user
user1 = User(name="Eshan Jain", email="eshanjain@udacity.com",
             picture='https://goo.gl/zxg5oL')
session.add(user1)
session.commit()

# pop marvel universe characters
category1 = Category(name="Popular Marvel Characters", user_id=1)
session.add(category1)
session.commit()

char1 = CatChar(name="Iron Man", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char1)
session.commit()

char2 = CatChar(name="Banner", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char2)
session.commit()

char3 = CatChar(name="Hulk", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char3)
session.commit()

char4 = CatChar(name="Captain America", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char4)
session.commit()

char5 = CatChar(name="Warewolf", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char5)
session.commit()

char6 = CatChar(name="Peter Parker", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char6)
session.commit()

char7 = CatChar(name="Spiderman", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char7)
session.commit()

char8 = CatChar(name="Black Panther", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category1)
session.add(char8)
session.commit()

# pop dc universe characters
category2 = Category(name="Popular DC Characters", user_id=1)

session.add(category2)
session.commit()

char1 = CatChar(name="Flash", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char1)
session.commit()

char2 = CatChar(name="Wonderwomen", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char2)
session.commit()

char3 = CatChar(name="Superman", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char3)
session.commit()

char4 = CatChar(name="Batman", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char4)
session.commit()

char5 = CatChar(name="Green Lantern", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char5)
session.commit()

char6 = CatChar(name="Cyborg", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char6)
session.commit()

char7 = CatChar(name="Aquaman", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category2)
session.add(char7)
session.commit()

# marvel uni groups
category3 = Category(name="Marvel Universe Teams", user_id=1)

session.add(char1)
session.commit()

char1 = CatChar(name="Avengers", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category3)
session.add(char1)
session.commit()

char2 = CatChar(name="X-Men", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category3)
session.add(char2)
session.commit()

char3 = CatChar(name="Fantastic Four", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category3)
session.add(char3)
session.commit()

char4 = CatChar(name="Guardians of the Galaxy", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category3)
session.add(char4)
session.commit()

# dc uni groups
category4 = Category(name="DC Universe Teams", user_id=1)

session.add(category4)
session.commit()

char1 = CatChar(name="Justice League", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category4)
session.add(char1)
session.commit()

char2 = CatChar(name="Suicide Squad", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category4)
session.add(char2)
session.commit()

char3 = CatChar(name="Green Lanern Corps", user_id=1,
                description="Lorem ipsum dolor sit amet. ", category=category4)
session.add(char3)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
