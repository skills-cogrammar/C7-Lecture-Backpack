from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey
from env_variables import USER_TABLE_NAME, COMMENT_TABLE_NAME, PROFILE_TABLE_NAME

Base = declarative_base()

class User(Base):
    __tablename__ = USER_TABLE_NAME
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)
    comment: Mapped["Comment"] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    def __repr__(self):
        return f"{self.name}"
    
class Profile(Base):
    __tablename__ = PROFILE_TABLE_NAME
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"{self.profile}"
    

class Comment(Base):
    __tablename__ = COMMENT_TABLE_NAME
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship(back_populates="comment")

    def __repr__(self):
        return f"{self.comment}"
    
