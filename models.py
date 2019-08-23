from mongoengine import *
connect("lesson_9")

class User(Document):

    login = StringField(max_length=30, unique=True)
    passwd = StringField(min_length=8)
    email = EmailField(unique=True)
    role = StringField()

class Category(EmbeddedDocument):

    title = StringField(max_length=255)
    desc = StringField(max_lenght=1024)

class Item(Document):

    added_by = ReferenceField(User)
    category = EmbeddedDocumentField(Category)
    is_available = BooleanField(default=True)
    name = StringField(required=True, max_length=255)
    desc = StringField(max_length=2048, required=False)
    weight = FloatField(required=False)

    @classmethod
    def create_new_item(cls, **kwargs):
        new_obj = cls(**kwargs)


#user = {"login": "test_user", "passwd": "123Aaavvv",
#                "email": "aaaA@gmail.com", "role": "admin"}
#user_obj = User(**user)
#user = user_obj.save()
#print(user.id)

#category = {"title": "Fruits", "desc": "Here is some fruits"}
#category_obj = Category(**category)
#category = category_obj.save()
#item = {"added_by": user, "category": category, "is_available": True,
#        "name": "orange"}
#litem = Item(**item).save()

#items = Item.objects(id="5d5c33f687d71c305854ef1c")
items = Item.objects.filter(category="5d5c33f687d71c305854ef1b")
for i in items:
    print(i.id)
