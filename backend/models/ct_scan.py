from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.database import Base


class CTScan(Base):
    __tablename__ = "ct_scans"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    file_name = Column(String(255), nullable=False)

    file_type = Column(String(20), nullable=False)

    file_path = Column(String(500), nullable=False)

    uploaded_at = Column(
        DateTime,
        server_default=func.now()
    )

    user = relationship(
        "User",
        back_populates="ct_scans"
    )