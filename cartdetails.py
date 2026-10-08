from playwright.sync_api import Page


class cart_details:
    def __init__(self,page:Page):
        self.page = page
        self.cart = page.locator(".shopping_cart_link")

        self.checkout = page.get_by_role("button", name="Checkout")

    def get_cart_details(self):
        self.cart.click()
        assert self.page.locator(".inventory_item_name").filter(has_text="Sauce Labs Backpack")

        assert self.page.locator(".inventory_item_price").filter(has_text="$29.99")

        self.checkout.click()

