from sqlalchemy.orm import Session
import models
from datetime import datetime
def list_vendors(db: Session): return db.query(models.Vendor).order_by(models.Vendor.id).all()
def create_vendor(db: Session, payload: dict):
    v = models.Vendor(**payload); db.add(v); db.commit(); db.refresh(v); return v
def list_products(db: Session): return db.query(models.Product).order_by(models.Product.id).all()
def create_product(db: Session, payload: dict):
    p = models.Product(**payload); db.add(p); db.commit(); db.refresh(p); return p
def list_warehouses(db: Session): return db.query(models.Warehouse).order_by(models.Warehouse.id).all()
def create_warehouse(db: Session, payload: dict):
    w = models.Warehouse(**payload); db.add(w); db.commit(); db.refresh(w); return w
def list_sales_orders(db: Session): return db.query(models.SalesOrder).order_by(models.SalesOrder.id).all()
def create_sales_order(db: Session, payload: dict):
    so = models.SalesOrder(**payload); db.add(so); db.commit(); db.refresh(so); return so
def list_purchase_orders(db: Session): return db.query(models.PurchaseOrder).order_by(models.PurchaseOrder.id).all()
def create_purchase_order(db: Session, payload: dict):
    po = models.PurchaseOrder(**payload); db.add(po); db.commit(); db.refresh(po); return po
def list_inventory(db: Session): return db.query(models.Inventory).order_by(models.Inventory.id).all()
def upsert_inventory(db: Session, payload: dict):
    pid = int(payload.get('product_id')); wid = int(payload.get('warehouse_id')); qty = float(payload.get('quantity',0))
    item = db.query(models.Inventory).filter(models.Inventory.product_id==pid, models.Inventory.warehouse_id==wid).first()
    if item:
        item.quantity = item.quantity + qty; item.last_updated = datetime.utcnow()
    else:
        item = models.Inventory(product_id=pid, warehouse_id=wid, quantity=qty); db.add(item)
    db.commit(); db.refresh(item); return item
def list_transactions(db: Session): return db.query(models.Transaction).order_by(models.Transaction.id).all()
def create_transaction(db: Session, payload: dict):
    t = models.Transaction(**payload); db.add(t); db.commit(); db.refresh(t); return t
def list_pl_snapshots(db: Session): return db.query(models.PLSnapshot).order_by(models.PLSnapshot.id.desc()).all()
def create_pl_snapshot(db: Session, payload: dict):
    snap = models.PLSnapshot(**payload); db.add(snap); db.commit(); db.refresh(snap); return snap
def list_kpis(db: Session): return db.query(models.KPI).order_by(models.KPI.id.desc()).all()
def create_kpi(db: Session, payload: dict):
    k = models.KPI(**payload); db.add(k); db.commit(); db.refresh(k); return k
