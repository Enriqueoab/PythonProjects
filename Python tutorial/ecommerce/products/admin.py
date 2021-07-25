from django.contrib import admin
from .models import Product,Offer


# That way we set a table view of our products in our
# admin view in the web
class ProductAdmin(admin.ModelAdmin):
    
    # list_display it's override from ModelAdmin
    # Names ofeach column that we want to show
    list_display=('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    
    # list_display it's override from ModelAdmin
    # Names ofeach column that we want to show
    list_display=('code','description','discount')

# We pass our Product class as an argument to
# tell Django that we want to administrate
# from the administration panel

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)






