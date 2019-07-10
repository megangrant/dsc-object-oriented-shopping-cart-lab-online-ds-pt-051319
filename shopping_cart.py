class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.emp_discount = emp_discount
        self.items = []
        
        
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total
    
    
    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        for i in self.items:
            prices = [i["price"]]
        length = len(prices)
        if (length%2 == 0):
            mid_right = int(length/2)
            mid_left = mid_right - 1
            median = (prices[mid_left] + prices[mid_right])/2
            return median
        else:
            mid = int(length/2)
            return prices[mid]

    def apply_discount(self):
        if self.emp_discount:
            discount = self.emp_discount/100
            disc_total = self.total * (1 - discount)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']