from django.db import models

# ১. ডিভিশন
class Division(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

# ২. জোন
class Zone(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

# ৩. এরিয়া
class Area(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

# ৪. রুট
class Route(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

# ৫. আউটলেট
class Outlet(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    def __str__(self): return self.name

# ৬. প্রোডাক্ট
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)