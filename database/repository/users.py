from sqlalchemy.orm import Session
from schemas.users import UserCreate
from database.models.users import User
from core.hashing import Hasher

def create_new_user(db: Session, user: UserCreate) -> User:
    """
    Creates a new user in the database with the specified user data.

    Args:
        db (Session): The SQLAlchemy database session.
        user (UserCreate): The user data to create the user with.

    Returns:
        User: The created user object.
    """

    # Hash the user password using the Hasher class.
    hashed_password = Hasher.get_password_hash(user.password)

    # Create a new User object with the specified user data and hashed password.
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True,
        is_superuser=False,
    )

    # Add the new user object to the database, commit the transaction, and refresh the user object.
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Return the created user object.
    return db_user
