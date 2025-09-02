from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
router = APIRouter()
def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()
@router.get('/vendors')
def vendors(db: Session = Depends(get_db)):
    return crud.list_vendors(db)
@router.post('/vendors')
def add_vendor(payload: dict, db: Session = Depends(get_db)):
    return crud.create_vendor(db, payload)
@router.get('/products')
def products(db: Session = Depends(get_db)):
    return crud.list_products(db)
@router.post('/products')
def add_product(payload: dict, db: Session = Depends(get_db)):
    return crud.create_product(db, payload)
@router.get('/warehouses')
def warehouses(db: Session = Depends(get_db)):
    return crud.list_warehouses(db)
@router.post('/warehouses')
def add_warehouse(payload: dict, db: Session = Depends(get_db)):
    return crud.create_warehouse(db, payload)
