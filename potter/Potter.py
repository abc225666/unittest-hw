class Potter:
    BOOK_LIST = ["book1", "book2", "book3", "book4", "book5"]

    def __init__(self):
        self.book_cart = {}

    def get_cart(self):
        return self.book_cart

    def add_cart(self, books):
        # books type is {"book1": amount, "book2": amount....}
        for k,v in books.items():
            if k not in self.BOOK_LIST:
                continue

            if k not in self.book_cart:
                self.book_cart[k] = 0
            self.book_cart[k] += v


    def get_price(self):
        # get final price with discount
        total = 0
        for k, v in self.book_cart.items():
            total += 8 * v

        return total
