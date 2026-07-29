from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.ct_scan import CTScan
from backend.models.user import User
from backend.schemas.ct_scan import CTScanResponse
from backend.auth.jwt_handler import get_current_user

router = APIRouter(
    prefix="/ct-scans",
    tags=["CT Scans"]
)

# Upload folders
UPLOAD_DIR = Path("uploads")
DICOM_DIR = UPLOAD_DIR / "dicom"
PHOTO_DIR = UPLOAD_DIR / "photos"


@router.post("/upload", response_model=CTScanResponse)
def upload_ct_scan(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload CT Scan (DICOM or Photo)
    Logic will be added in the next step.
    """

@router.post("/upload", response_model=CTScanResponse)
def upload_ct_scan(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Supported extensions
    allowed_extensions = {
        ".dcm": "dicom",
        ".jpg": "photo",
        ".jpeg": "photo",
        ".png": "photo"
    }

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )

    file_type = allowed_extensions[extension]

    # Generate unique filename
    unique_name = f"{uuid.uuid4()}{extension}"

    # Select save folder
    if file_type == "dicom":
        save_path = DICOM_DIR / unique_name
    else:
        save_path = PHOTO_DIR / unique_name

    # Save file
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save to database
    new_scan = CTScan(
        user_id=current_user.id,
        file_name=file.filename,
        file_type=file_type,
        file_path=str(save_path)
    )

    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)

    return new_scan

from typing import List


@router.get("/my-scans", response_model=List[CTScanResponse])
def get_my_scans(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    scans = (
        db.query(CTScan)
        .filter(CTScan.user_id == current_user.id)
        .order_by(CTScan.uploaded_at.desc())
        .all()
    )

    return scans