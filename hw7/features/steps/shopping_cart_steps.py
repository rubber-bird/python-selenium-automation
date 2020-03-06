from behave import then

@then('Verify {text} text present')
def verify_text_present(context, text):
    context.app.shopping_cart_page.verify_empty_cart(text)