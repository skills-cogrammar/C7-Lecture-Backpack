from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base
from env_variables import DB_NAME

engine = create_engine(f"sqlite:///{DB_NAME}", echo=True)
session = Session(engine)
Base.metadata.create_all(engine)