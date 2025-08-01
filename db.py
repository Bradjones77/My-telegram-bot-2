from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///trades.db")
Base = declarative_base()

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    coin = Column(String)
    action = Column(String)  # BUY or SELL
    stop_loss = Column(Float)
    confidence = Column(Float)
    trade_type = Column(String)  # short or long
    entered = Column(Boolean, default=False)

Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
