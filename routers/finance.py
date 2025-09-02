from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
router = APIRouter()
def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()
@router.get('/transactions')
def transactions(db: Session = Depends(get_db)):
    return crud.list_transactions(db)
@router.post('/transactions')
def create_transaction(payload: dict, db: Session = Depends(get_db)):
    return crud.create_transaction(db, payload)
@router.get('/pl_snapshots')
def pl_snapshots(db: Session = Depends(get_db)):
    return crud.list_pl_snapshots(db)
@router.post('/pl_snapshots')
def create_pl_snapshot(payload: dict, db: Session = Depends(get_db)):
    return crud.create_pl_snapshot(db, payload)
@router.get('/kpis')
def kpis(db: Session = Depends(get_db)):
    return crud.list_kpis(db)
@router.post('/kpis')
def create_kpi(payload: dict, db: Session = Depends(get_db)):
    return crud.create_kpi(db, payload)
