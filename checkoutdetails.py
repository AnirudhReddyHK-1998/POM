

class CheckoutDetails:
    def __init__(self, page):
        self.page = page
        self.firstname = page.get_by_placeholder("First Name")
        self.lastname = page.get_by_placeholder("Last Name")
        self.zipcode = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")

    def checkout_details(self):
        self.firstname.fill("anirudh")
        self.lastname.fill("reddy")
        self.zipcode.fill("123456")
        self.page.locator("#continue").click()