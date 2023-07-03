from seleniumbase import BaseCase
import pytest

class SwagLabsTests(BaseCase):
    def login_to_swag_labs(self, username="standard_user",pwd="secret_sauce"):
        """Login to Swag Labs and verify success."""
        self.open("https://www.saucedemo.com")
        if username not in self.get_text("#login_credentials"):
            self.fail("Invalid user for login: %s" % username)
        self.type("#user-name", username)
        self.type("#password", pwd)
        self.click('input[type="submit"]')
        self.assert_element("div.inventory_list")
        self.assert_element('.inventory_item:contains("Sauce Labs Backpack")')

    @pytest.mark.expected_failure
    def test_1_wronguser(self):
        self.login_to_swag_labs(username="standard_user123")

    @pytest.mark.expected_failure
    def test_2_wrongpwd(self):
        self.login_to_swag_labs(username="standard_user123",pwd="secret_sauce")

    def test_3(self):
        """This test checks functional flow of the Swag Labs store."""
        self.login_to_swag_labs(username="standard_user")

        # Verify that the "Test.allTheThings() T-Shirt" appears on the page
        item_name = "Test.allTheThings() T-Shirt"
        self.assert_text(item_name)

        # Verify that a reverse-alphabetical sort works as expected
        self.select_option_by_value("select.product_sort_container", "za")
        if item_name not in self.get_text("div.inventory_item"):
            self.fail('Sort Failed! Expecting "%s" on top!' % item_name)

    @pytest.mark.expected_failure
    def test_4_failcart(self):
        self.test_3()
        # Add the "Test.allTheThings() T-Shirt" to the cart
        self.assert_exact_text("cart", "button.btn_inventory")
        item_price = self.get_text("div.inventory_item_price")
        self.click("button.btn_inventory")
        self.assert_exact_text("REMOVE", "button.btn_inventory")
        self.assert_exact_text("1", "span.shopping_cart_badge")

    def test_5_addcart(self):
        self.test_3()
        item_name = "Test.allTheThings() T-Shirt"
        # Add the "Test.allTheThings() T-Shirt" to the cart
        self.assert_exact_text("ADD TO CART", "button.btn_inventory")
        item_price = self.get_text("div.inventory_item_price")
        self.click("button.btn_inventory")
        self.assert_exact_text("REMOVE", "button.btn_inventory")
        self.assert_exact_text("1", "span.shopping_cart_badge")

    @pytest.mark.expected_failure
    def test_6_failverify(self):
        self.test_5_addcart()
        # Verify your cart
        self.click("#shopping_cart_container a")
        self.assert_element('span:contains("cart")')
        self.assert_text(item_name, "div.inventory_item_name")
        self.assert_exact_text("1", "div.cart_quantity")
        self.assert_exact_text("REMOVE", "button.cart_button")
        self.assert_element("button#continue-shopping")

    def test_7(self):
        self.test_5_addcart()
        item_name = "Test.allTheThings() T-Shirt"
        item_price = self.get_text("div.inventory_item_price")

        # Verify your cart
        self.click("#shopping_cart_container a")
        self.assert_element('span:contains("Your Cart")')
        self.assert_text(item_name, "div.inventory_item_name")
        self.assert_exact_text("1", "div.cart_quantity")
        self.assert_exact_text("REMOVE", "button.cart_button")
        self.assert_element("button#continue-shopping")

        # Checkout - Add info
        self.click("button#checkout")
        self.assert_element('span:contains("Checkout: Your Information")')
        self.assert_element("button#cancel")
        self.type("#first-name", "SeleniumBase")
        self.type("#last-name", "Rocks")
        self.type("#postal-code", "01720")

        # Checkout - Overview
        self.click("input#continue")
        self.assert_element('span:contains("Checkout: Overview")')
        self.assert_element("button#cancel")
        self.assert_text(item_name, "div.inventory_item_name")
        self.assert_text(item_price, "div.inventory_item_price")
        self.assert_exact_text("1", "div.cart_quantity")

    def test_8_submit(self):
        self.test_7()
        # Finish Checkout and verify that the cart is now empty
        self.click("button#finish")
        self.assert_exact_text("THANK YOU FOR YOUR ORDER", "h2")
        self.click("#shopping_cart_container a")
        self.assert_element_absent("div.inventory_item_name")
        self.click("button#continue-shopping")
        self.assert_element_absent("span.shopping_cart_badge")


    def test_9_verifybooking(self):
        self.test_3()

    @pytest.mark.expected_failure
    def test_10_login(self):
        self.login_to_swag_labs(username="avcd",pwd="asdasa")

    def tearDown(self):
        self.save_teardown_screenshot()  # Only if a test fails
        # Reset App State and Logout if the controls are present
        try:
            self.js_click_if_present("a#reset_sidebar_link")
            self.js_click_if_present("a#logout_sidebar_link")
        except Exception:
            pass
        super(SwagLabsTests, self).tearDown()

