from playwright.sync_api import Page


class cart_details:
    def __init__(self,page:Page):
        self.page = page
        self.cart = page.locator(".shopping_cart_link")

        self.checkout = page.get_by_role("button", name="Checkout")

    def get_cart_details(self):
        self.cart.click()
        product_name = self.page.locator(".inventory_item_name").text_content()
        assert product_name == "Sauce Labs Backpack"
        product_price = self.page.locator(".inventory_item_price").text_content()
        assert product_price == "$29.99"
        self.checkout.click()

