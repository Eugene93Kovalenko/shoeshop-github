from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to="category/%Y/%m/%d/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_app:category", kwargs={"category_name": self.name.lower()})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Gender(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to="gender/%Y/%m/%d/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гендер"
        verbose_name_plural = "Гендеры"


class Style(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Size(models.Model):
    name = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"


class Material(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_visits = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, related_name="products", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"product_slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("orders:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={"slug": self.slug})

    def get_gender_url(self):
        return reverse("products:gender", kwargs={"gender_slug": self.gender.name})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_variation')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product', 'size')
        verbose_name = "Товар | Размер"
        verbose_name_plural = "Товар | Размер"

    def __str__(self):
        return f"{self.product} / {self.size} size"


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product/%Y/%m/%d/")
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"

    def __str__(self):
        return self.image.name

    def get_absolute_url(self):
        return self.image.url
