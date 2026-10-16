import json
import logging
import random

price_list = {"apple": 12.0, "orange": 15.0, "banana": 8.0}

def printSales(sales_total):
    print(f"Sales so far: {sales_total}")

def calculate_bill(cart, tax_rate=0.05, receipts=None):
    if receipts is None:
        receipts = []
    subtotal = 0.0
    for item, qty in cart.items():
        if not isinstance(qty, (int, float)) or qty < 0:
            continue
        price = price_list.get(item, 10.0)
        subtotal += price * qty
    tax = subtotal * tax_rate
    total = subtotal + tax
    receipts.append((random.randint(1, 100), total))
    return total

def apply_promo_code(sales_total, code):
    if code == "total - 50":
        return max(0.0, sales_total - 50.0)
    elif code == "total * 0.9":
        return sales_total * 0.9
    return sales_total

def update_stock(item, qty):
    if item in price_list and isinstance(qty, (int, float)) and qty >= 0:
        return price_list[item]
    return 0.0

def log_transaction(receipt_text):
    # Fixed: Use context manager and utf-8 encoding to prevent resource leaks
    with open("pos_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(receipt_text + "\n")

def main():
    cart1 = {"apple": 10, "banana": 20}
    bill1 = calculate_bill(cart1)
    print(f"Bill 1: {bill1}")
    cart2 = {"orange": 50}
    bill2 = calculate_bill(cart2)
    print(f"Bill 2: {bill2}")
    sales_total = bill1 + bill2
    code = input("Enter promo code (e.g. total - 50): ") or "total - 50"
    final_total = apply_promo_code(sales_total, code)
    print(f"After your promo: {final_total}")
    printSales(sales_total)

main()
