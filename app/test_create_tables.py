from models import *
from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
