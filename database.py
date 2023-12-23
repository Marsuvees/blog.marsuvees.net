from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import bcrypt
from uuid import uuid4


Base = declarative_base()

try:
    engine = create_engine("postgresql://marsuvees:987654321@localhost:5432/blog_marsuvees")
except:
    print("Dropping to sqlite3")
    engine = create_engine("sqlite:///blog_marsuvees.db")
session = sessionmaker(engine)()

def uuid():
    return str(uuid4())

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    uuid = Column(String, nullable=False, default=uuid)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    phone_number = Column(String, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    password = Column(String, nullable=False)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(length=100), nullable=False)
    content = Column(String, nullable=False)
    post_datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    tags = relationship("Tag", secondary="blog_tag_association", back_populates="posts")

    def __repr__(self):
        return f"<Post(title={self.title})>"

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    post_datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    author_id = Column(ForeignKey("users.id"))
    post_id = Column(ForeignKey("posts.id"))

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", secondary="blog_tag_association", back_populates="tags")

    def __repr__(self):
        return f"<Tag(tag = {self.name})>"

blog_post_tag_association = Table(
    'blog_tag_association',
    Base.metadata,
    Column('blog_post_id', ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    admin = User(username="admin", password=bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))
    session.add(admin)
    tag1 = Tag(name="welcome")
    tag2 = Tag(name="first")
    # session.add_all((tag1, tag2))
    welcome_post = Post(title="Welcome to blog.marsuvees", content="This is the default welcome post", author_id=1, post_datetime= datetime.now(), tags=[tag1, tag2]) 
    # test_comment = Comment(content="this is a test of the comments.", author_id=1, post_id=1)
    # session.add(welcome_post)
    # session.add(test_comment)
    session.commit()


    