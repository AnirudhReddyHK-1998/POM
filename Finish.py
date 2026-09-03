from playwright.sync_api import Page, expect


class finishpage:
    def __init__(self, page:Page):
        self.page = page

        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")
        self.card = page.locator("div.summary_value_label").filter(has_text="SauceCard")
        self.tax = page.locator(".summary_tax_label").filter(has_text="Tax")
        self.total = page.locator(".summary_total_label").filter(has_text="Total")
        self.finish = page.get_by_role("button", name="Finish")
        self.thankyou = page.get_by_text("Thank you for your order!")
        self.confirm = page.locator(".complete-header")

    def final_finish(self):
        product_name = self.product_name.text_content()
        assert product_name == "Sauce Labs Backpack"
        product_price = self.product_price.text_content()
        assert product_price == "$29.99"
        card = self.card.text_content()
        assert card == "SauceCard #31337"
        tax = self.tax.text_content()
        assert tax == "Tax: $2.40"
        total = self.total.text_content()
        assert total == "Total: $32.39"
        self.finish.click()
        expect(self.thankyou).to_be_visible()
        confirm = self.confirm.all_text_contents()
        print(confirm)


