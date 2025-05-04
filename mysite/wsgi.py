import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_catlog.settings')  # Use your actual project settings

application = get_wsgi_application()
