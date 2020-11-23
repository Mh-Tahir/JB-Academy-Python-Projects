from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///list.db')
Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def choose():
  while True:
    command = input('\n1) Today\'s tasks\n2) Add task\n0) Exit\n')
    if command == '0':
        print('\nBye!')
        break
    elif command == '1':
        return show()
    elif command == '2':
        return add()

def show():
  rows = session.query(Table).all()
  print('\nToday:')
  if len(rows) == 0:
    print('Nothing to do!')
  else:
    n = 1
    for x in rows:
        print(f'{n}. {x}')
        n += 1
  choose()

def add():
  task = input('\nEnter task\n')
  new_row = Table(task=task)
  session.add(new_row)
  session.commit()
  print('The task has been added!')
  choose()

choose()

