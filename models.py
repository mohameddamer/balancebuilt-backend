from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
class Customer(Base):
    __tablename__='customers'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False); email=Column(String); phone=Column(String); address=Column(String); country=Column(String); created_at=Column(DateTime,default=datetime.utcnow)
class Vendor(Base):
    __tablename__='vendors'
    id=Column(Integer,primary_key=True,index=True); name=Column(String,nullable=False); email=Column(String); phone=Column(String); address=Column(String); country=Column(String); tax_id=Column(String); contact_person=Column(String); payment_terms=Column(String); status=Column(String,default='active'); created_at=Column(DateTime,default=datetime.utcnow)
class Product(Base):
    __tablename__='products'
    id=Column(Integer,primary_key=True,index=True); sku=Column(String,unique=True); name=Column(String,nullable=False); description=Column(Text); category=Column(String); unit_price=Column(Float,default=0.0); unit_cost=Column(Float,default=0.0); supplier_id=Column(Integer,ForeignKey('vendors.id')); reorder_level=Column(Float,default=0.0); ean=Column(String); active=Column(Boolean,default=True)
    supplier = relationship("Vendor", foreign_keys=[supplier_id])
class Warehouse(Base):
    __tablename__='warehouses'
    id=Column(Integer,primary_key=True,index=True); name=Column(String,nullable=False); location=Column(String); capacity=Column(Float); manager=Column(String); contact=Column(String); active=Column(Boolean,default=True)
class Inventory(Base):
    __tablename__='inventory'
    id=Column(Integer,primary_key=True,index=True); product_id=Column(Integer,ForeignKey('products.id')); warehouse_id=Column(Integer,ForeignKey('warehouses.id')); quantity=Column(Float,default=0.0); reserved=Column(Float,default=0.0); safety_stock=Column(Float,default=0.0); lead_time_days=Column(Integer,default=0); last_updated=Column(DateTime,default=datetime.utcnow)
    product = relationship("Product"); warehouse = relationship("Warehouse")
class SalesOrder(Base):
    __tablename__='sales_orders'
    id=Column(Integer,primary_key=True,index=True); customer_name=Column(String); customer_id=Column(Integer,ForeignKey('customers.id')); order_date=Column(DateTime,default=datetime.utcnow); delivery_date=Column(DateTime); status=Column(String,default='draft'); currency=Column(String,default='USD'); total_amount=Column(Float,default=0.0); notes=Column(Text)
class SalesOrderLine(Base):
    __tablename__='sales_order_lines'
    id=Column(Integer,primary_key=True,index=True); order_id=Column(Integer,ForeignKey('sales_orders.id')); product_id=Column(Integer,ForeignKey('products.id')); description=Column(String); quantity=Column(Float,default=1.0); unit_price=Column(Float,default=0.0); line_total=Column(Float,default=0.0)
class PurchaseOrder(Base):
    __tablename__='purchase_orders'
    id=Column(Integer,primary_key=True,index=True); vendor_id=Column(Integer,ForeignKey('vendors.id')); order_date=Column(DateTime,default=datetime.utcnow); delivery_date=Column(DateTime); status=Column(String,default='draft'); currency=Column(String,default='USD'); total_amount=Column(Float,default=0.0); notes=Column(Text)
class PurchaseOrderLine(Base):
    __tablename__='purchase_order_lines'
    id=Column(Integer,primary_key=True,index=True); order_id=Column(Integer,ForeignKey('purchase_orders.id')); product_id=Column(Integer,ForeignKey('products.id')); quantity=Column(Float,default=1.0); unit_cost=Column(Float,default=0.0); line_total=Column(Float,default=0.0)
class Transaction(Base):
    __tablename__='transactions'
    id=Column(Integer,primary_key=True,index=True); date=Column(DateTime,default=datetime.utcnow); txn_type=Column(String); account=Column(String); description=Column(Text); amount=Column(Float,default=0.0); currency=Column(String,default='USD'); fx_rate=Column(Float,default=1.0); related_order=Column(String)
class JournalEntry(Base):
    __tablename__='journal_entries'
    id=Column(Integer,primary_key=True,index=True); account=Column(String); debit=Column(Float,default=0.0); credit=Column(Float,default=0.0); date=Column(DateTime,default=datetime.utcnow); description=Column(Text)
class PLSnapshot(Base):
    __tablename__='pl_snapshots'
    id=Column(Integer,primary_key=True,index=True); period_start=Column(DateTime); period_end=Column(DateTime); total_revenue=Column(Float,default=0.0); subscription_income=Column(Float,default=0.0); other_income=Column(Float,default=0.0); raw_materials=Column(Float,default=0.0); inventory_cost=Column(Float,default=0.0); production_cost=Column(Float,default=0.0); shipping_cost=Column(Float,default=0.0); salaries=Column(Float,default=0.0); rent=Column(Float,default=0.0); marketing=Column(Float,default=0.0); software=Column(Float,default=0.0); interest=Column(Float,default=0.0); taxes=Column(Float,default=0.0); depreciation=Column(Float,default=0.0); amortization=Column(Float,default=0.0); fx_gain_loss=Column(Float,default=0.0); base_currency=Column(String,default='USD'); gross_profit=Column(Float,default=0.0); operating_profit=Column(Float,default=0.0); net_profit=Column(Float,default=0.0); created_at=Column(DateTime,default=datetime.utcnow)
class KPI(Base):
    __tablename__='kpis'
    id=Column(Integer,primary_key=True,index=True); name=Column(String); value=Column(Float); note=Column(String); date=Column(DateTime,default=datetime.utcnow)
