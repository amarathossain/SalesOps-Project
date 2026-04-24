from django.contrib import admin
from .models import Product, Division, Zone, Area, Route, Outlet

# সব মডেল অ্যাডমিন প্যানেলে রেজিস্টার করা হচ্ছে
admin.site.register(Product)
admin.site.register(Division)
admin.site.register(Zone)
admin.site.register(Area)
admin.site.register(Route)
admin.site.register(Outlet)