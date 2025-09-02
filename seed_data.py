from database import SessionLocal, init_db
import models
from datetime import datetime
def seed():
    init_db()
    db = SessionLocal()
    if db.query(models.Vendor).count() == 0:
        db.add(models.Vendor(name='ABC Supplies', email='abc@supplies.com', phone='+1-555-1234', address='123 Market St', country='USA', tax_id='TAX-112233', contact_person='John Smith', payment_terms='Net 30'))
    if db.query(models.Product).count() == 0:
        db.add(models.Product(sku='WGT-001', name='Widget A', description='Example widget', category='Electronics', unit_price=50.0, unit_cost=30.0, supplier_id=1, reorder_level=100))
    if db.query(models.Warehouse).count() == 0:
        db.add(models.Warehouse(name='Main WH', location='NY, USA', capacity=10000, manager='Alice Johnson', contact='alice@wh.com'))
    if db.query(models.Inventory).count() == 0:
        db.add(models.Inventory(product_id=1, warehouse_id=1, quantity=1200, safety_stock=100, lead_time_days=7))
    if db.query(models.SalesOrder).count() == 0:
        db.add(models.SalesOrder(customer_name='John Doe', total_amount=500.0))
    if db.query(models.PurchaseOrder).count() == 0:
        db.add(models.PurchaseOrder(vendor_id=1, total_amount=4500.0))
    if db.query(models.Transaction).count() == 0:
        db.add(models.Transaction(txn_type='expense', account='Office Supplies', description='Stationery', amount=300.0, currency='USD'))
    db.commit(); db.close(); print('seed complete')
if __name__=='__main__': seed()
