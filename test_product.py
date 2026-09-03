from playwright.sync_api import Page

from POM import checkoutdetails
from POM.Finish import  finishpage
from POM.Login_page import loging_page
from POM.Product_cart import product_cart
from POM.cartdetails import cart_details
from POM.checkoutdetails import CheckoutDetails
from POM.config import username, password


def test_product(page:Page):
    #login
    login = loging_page(page)
    login.login(username,password)

    #adding product to cart
    cart = product_cart(page)
    cart.Cart()

    #verifying cart product details and checkout
    cartdetails = cart_details(page)
    cartdetails.get_cart_details()

    #checkout details
    checkout = CheckoutDetails(page)
    checkout.checkout_details()

    #finish
    finish = finishpage(page)
    finish.final_finish()


