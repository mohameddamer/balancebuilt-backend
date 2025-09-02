from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import csv, io, models
router = APIRouter()
def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()
@router.post('/vendors')
async def upload_vendors(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = (await file.read()).decode('utf-8')
    reader = csv.DictReader(io.StringIO(content))
    created = 0
    for row in reader:
        v = models.Vendor(name=row.get('name'), email=row.get('email'), phone=row.get('phone'), address=row.get('address'), country=row.get('country'), tax_id=row.get('tax_id'), contact_person=row.get('contact_person'), payment_terms=row.get('payment_terms'))
        db.add(v); created += 1
    db.commit(); return {'created': created}
@router.post('/products')
async def upload_products(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = (await file.read()).decode('utf-8')
    reader = csv.DictReader(io.StringIO(content))
    created = 0
    for row in reader:
        p = models.Product(sku=row.get('sku'), name=row.get('name'), description=row.get('description'), category=row.get('category'), unit_price=float(row.get('unit_price') or 0), unit_cost=float(row.get('unit_cost') or 0), supplier_id=int(row.get('supplier_id')) if row.get('supplier_id') else None)
        db.add(p); created += 1
    db.commit(); return {'created': created}
@router.post('/inventory')
async def upload_inventory(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = (await file.read()).decode('utf-8')
    reader = csv.DictReader(io.StringIO(content))
    processed = 0
    for row in reader:
        pid = int(row.get('product_id')); wid = int(row.get('warehouse_id')); qty = float(row.get('quantity') or 0)
        item = db.query(models.Inventory).filter(models.Inventory.product_id==pid, models.Inventory.warehouse_id==wid).first()
        if item:
            item.quantity += qty
        else:
            item = models.Inventory(product_id=pid, warehouse_id=wid, quantity=qty); db.add(item)
        processed += 1
    db.commit(); return {'processed': processed}
