"""
 در این حالت اگر ما تخفیف را برابر باقیمت محصول یا بیش از ان قرار دهیم
 
 
 در این حالت شرط نادرست خواهد یود 

 در دست دیگر اگر کمتر از قیمت اصلی باشد به نوعی اسزت درست عمل کرده
"""

def apply_discount(price: int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""
    final_price = int(price * (1 - discount))
    if not (0 < final_price <= price):
        raise ValueError("Invalid final price: discount is too high!")
    return final_price



"""
  این دستور بیشتر برای بررسی‌های داخلی (مانند تست‌های توسعه‌دهنده) و دیباگ استفاده می‌شودو  برای اعتبارسنجی داده‌ها در محیط تولید
  مناسب نیست
"""

"""
زمانی که کد با فلگ 
-o
اجرا میشود دستور 
assert 
نادیده گرفته میشود و اگر اعتبارسنجی مهمی درون آنها قرار گرفته باشد، دیگر بررسی نخواهد شد.

"""