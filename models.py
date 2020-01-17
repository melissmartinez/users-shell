from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    s = '\n'
    s += f"first_name: {self.first_name}\n"
    s += f"last_name: {self.last_name}\n"
    s += f"email: {self.email}\n"
    s += f"age: {self.age}\n"
    s += f"password: {self.password}\n"
    return s

#Run the queiries in your terminal! 
# User.objects.create(first_name="Monty", last_name="Python", email="monty@python.com", age="44")
# User.objects.create(first_name="Ethan", last_name="Klien", email="monty@python.com", age="38")
# User.objects.create(first_name="Jordan", last_name="Amon", email="monty@python.com", age="25")
# User.objects.all()
# User.objects.first()
# User.objects.last()
# c=User.objects.get(id=3) c.last_name="Pancakes" c.save()
# c=User.objects.get(id=2) c.delete()
# Users.objects.order_by('first_name')