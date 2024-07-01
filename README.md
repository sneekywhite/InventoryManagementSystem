# InventoryManagementSystem

# Online Store Inventory and Supplier Management API

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## API Endpoints

- `/api/items/` - CRUD operations for inventory items
- `/api/suppliers/` - CRUD operations for suppliers

## Models

### Item
- `name`: string
- `description`: text
- `price`: decimal
- `quantity`: integer
- `date_added`: date
- `suppliers`: many-to-many relationship with Supplier

### Supplier
- `name`: string
- `contact_info`: text
- `items`: many-to-many relationship with Item
