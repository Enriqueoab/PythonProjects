from django.contrib import admin
from .models import Product

#That way we set a table view of our products in this case
class ProductAdmin(admin.ModelAdmin):
    
    # list_display it's override from ModelAdmin
    # Names ofeach column that we want to show
    list_display=('name','price','stock')

# We pass our Product class as an argument to
# tell Django that we want to administrate
# from the administration panel

admin.site.register(Product,ProductAdmin)





