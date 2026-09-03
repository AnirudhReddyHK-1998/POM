from playwright.sync_api import Page


class product_cart:

    def __init__(self, page: Page):
        self.page = page
        self.productname = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
        self.cart = self.productname.get_by_role("button", name="Add to cart")

    def Cart(self):
        self.cart.click()