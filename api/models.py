from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Individu(Base):
    __tablename__ = "Individu"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    death_date = Column(Date)
    __table_args__ = (
        CheckConstraint("death_date IS NULL OR death_date > birth_date", name="birth_before_death"),
    )


class Relations(Base):
    __tablename__ = "Relations"
    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("Individu.id", ondelete="CASCADE"), nullable=False)
    child_id = Column(Integer, ForeignKey("Individu.id", ondelete="CASCADE"), nullable=False)
    relation_type = Column(String, nullable=False)
    __table_args__ = (
        CheckConstraint("parent_id <> child_id", name="no_self_parenting"),
    )