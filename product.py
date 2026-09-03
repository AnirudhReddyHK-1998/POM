from playwright.sync_api import Page, expect


class product:

    def __init__(self, page:Page):
        self.page = page
        self.product_name = page.locator(".inventory_item_name")

    def product_view(self):
        products = self.product_name.all_text_contents()
        for products in products:
            print(products)





