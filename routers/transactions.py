from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
router = APIRouter()
def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()
@router.get('/sales_orders')
def sales_orders(db: Session = Depends(get_db)):
    return crud.list_sales_orders(db)
@router.post('/sales_orders')
def create_sales_order(payload: dict, db: Session = Depends(get_db)):
    return crud.create_sales_order(db, payload)
@router.get('/purchase_orders')
def purchase_orders(db: Session = Depends(get_db)):
    return crud.list_purchase_orders(db)
@router.post('/purchase_orders')
def create_purchase_order(payload: dict, db: Session = Depends(get_db)):
    return crud.create_purchase_order(db, payload)
@router.get('/inventory')
def inventory(db: Session = Depends(get_db)):
    return crud.list_inventory(db)
@router.post('/inventory')
def upsert_inventory(payload: dict, db: Session = Depends(get_db)):
    return crud.upsert_inventory(db, payload)
