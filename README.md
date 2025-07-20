# PharmAssist - Pharmacy Management System

A comprehensive Django-based pharmacy management system with shopping cart functionality and OCR (Optical Character Recognition) capabilities for prescription processing.

## 🚀 Quick Start Demo

**Try the demo immediately after setup:**

1. Run the development server: `python manage.py runserver`
2. Go to admin panel: `http://127.0.0.1:8000/admin/`
3. **Login with**: Username: `admin` | Password: `1234`
4. Explore the pharmacy management features!

## 🚀 Features

- **Product Management**: Add, view, update, and remove pharmaceutical products
- **Inventory Tracking**: Monitor stock levels and expiry dates
- **Shopping Cart**: Add products to cart, manage quantities, and checkout
- **OCR Integration**: Extract text from prescription images using Tesseract
- **Low Stock Alerts**: Identify products with low inventory
- **Expiry Monitoring**: Track products nearing expiration
- **Patient Information**: Capture customer details during checkout
- **Invoice Generation**: Generate invoices for completed orders
- **Admin Panel**: Django admin interface for system management

## 🛠️ Technology Stack

- **Backend**: Django 5.0.6
- **Database**: MySQL
- **OCR Engine**: Tesseract OCR with pytesseract
- **Image Processing**: Pillow (PIL)
- **Server**: Gunicorn
- **Frontend**: HTML templates with Django templating
- **Environment**: Python virtual environment

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8+
- MySQL Server
- Tesseract OCR
- pip (Python package manager)

### Installing Tesseract OCR

**Windows:**

1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install and note the installation path
3. Update the tesseract path in `products/views.py` if needed

**Ubuntu/Debian:**

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**macOS:**

```bash
brew install tesseract
```

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saikrishna-avskr/rtfp-1.git
cd rtfp-1
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
cd pharmassit
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=pharmassist
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Django Configuration
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`

## � Demo Login Credentials

For demonstration purposes, use the following credentials to access the admin panel:

**Admin Login**:

- **Username**: `admin`
- **Password**: `Admin@1234`

_Note: These are demo credentials for testing purposes only. In production, use strong, unique passwords._

## �📁 Project Structure

```
rtfp-1/
├── .env                    # Environment variables
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── pharmassit/            # Main Django project
│   ├── manage.py          # Django management script
│   ├── requirements.txt   # Python dependencies
│   ├── pharmassit/        # Project configuration
│   │   ├── settings.py    # Django settings
│   │   ├── urls.py        # Main URL configuration
│   │   ├── wsgi.py        # WSGI configuration
│   │   └── asgi.py        # ASGI configuration
│   ├── products/          # Products app
│   │   ├── models.py      # Product data models
│   │   ├── views.py       # Product views & OCR logic
│   │   ├── urls.py        # Product URL patterns
│   │   └── templates/     # Product HTML templates
│   └── cart/              # Shopping cart app
│       ├── models.py      # Cart data models
│       ├── views.py       # Cart functionality
│       ├── urls.py        # Cart URL patterns
│       └── templates/     # Cart HTML templates
└── tobeadded/             # Additional OCR scripts
    ├── ocr.py             # Camera-based OCR
    ├── ocr2.py            # Enhanced OCR functionality
    └── ...                # Other OCR implementations
```

## 📊 Database Models

### Product Model

```python
class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    expiry_date = models.DateField()
    price = models.FloatField()
    stock = models.IntegerField()
    storage_loc = models.CharField(max_length=255)
    image = models.CharField(max_length=2083)
```

### Cart Model

```python
class Cart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    pid = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    tot_price = models.FloatField(null=True)
```

## 🔗 API Endpoints

### Products

- `/` - Home page
- `/products/details/` - Product listing and search
- `/products/find_exp_items/` - Find expiring products
- `/products/find_low_stock/` - Find low stock items
- `/products/remove_product/<int:pid>/` - Remove product
- `/products/show_upload/` - Upload prescription form
- `/products/upload_report/` - Process uploaded prescription

### Cart

- `/cart/add/<int:pid>/` - Add product to cart
- `/cart/remove/<int:pid>/` - Remove product from cart
- `/cart/show/` - View cart contents
- `/cart/update/<int:product_id>/` - Update cart quantity
- `/cart/clear/` - Clear entire cart
- `/cart/checkout/` - Checkout process
- `/cart/order/` - Process order

## 🖼️ OCR Functionality

The system includes OCR capabilities to process prescription images:

1. **Upload Prescription**: Users can upload prescription images
2. **Text Extraction**: Tesseract OCR extracts text from images
3. **Product Matching**: System matches extracted text with product database
4. **Auto-Add to Cart**: Matching products are automatically added to cart

### OCR Configuration

Update the Tesseract path in `products/views.py`:

```python
pytesseract.pytesseract.tesseract_cmd = 'path/to/tesseract.exe'
```

## 👥 User Roles

### Admin Users

- Access Django admin panel at `/admin/`
- **Demo Login**: Username: `admin`, Password: `1234`
- Manage products, inventory, and system settings
- View reports and analytics

### Regular Users

- Browse products
- Add items to cart
- Process orders
- Upload prescriptions

## 🚀 Deployment

### Production Settings

1. Set `DEBUG=False` in environment variables
2. Configure proper `ALLOWED_HOSTS`
3. Use production database (PostgreSQL recommended)
4. Configure static files serving
5. Use Gunicorn for WSGI server

### Example Production Command

```bash
gunicorn pharmassit.wsgi:application --bind 0.0.0.0:8000
```

## 🧪 Testing

Run tests using Django's test framework:

```bash
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔧 Troubleshooting

### Common Issues

1. **Tesseract Not Found**

   - Ensure Tesseract is installed and path is correctly set
   - Update the tesseract_cmd path in views.py

2. **Database Connection Error**

   - Verify MySQL is running
   - Check database credentials in .env file
   - Ensure database exists

3. **Import Errors**

   - Activate virtual environment
   - Install all requirements: `pip install -r requirements.txt`

4. **Static Files Not Loading**
   - Run: `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings

## 📞 Support

For support and questions:

- Create an issue on GitHub
- Contact: saikrishnaavskr@gmail.com

## 🙏 Acknowledgments

- Django Community for the excellent framework
- Tesseract OCR team for OCR capabilities
- Contributors and testers

---

**Note**: This is a development version. For production use, please implement proper security measures, error handling, and testing.
