print("\n===================================")
print("🍽️  Welcome to DevOps Café Menu")
print("===================================\n")

menu_items = {
    1: {"name": "Build & Brew Coffee", "price": "$2.99"},
    2: {"name": "Docker Donuts", "price": "$1.49"},
    3: {"name": "Kubernetes Kakes", "price": "$3.99"},
    4: {"name": "Pipeline Pizza", "price": "$5.49"},
    5: {"name": "CI/CD Soda", "price": "$0.99"},
}

for item_no, item in menu_items.items():
    print(f"{item_no}. {item['name']:<25} - {item['price']}")

print("\n🛒 Please place your order via Jenkins build!")
