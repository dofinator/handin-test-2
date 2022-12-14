from behave import *
import string_utility

@given('a lowercased string')
def step_impl(context):
    context.string = "asdf"

@when('the string is uppercased')
def step_impl(context):
    context.uppercased_string = string_utility.upper_letters(context.string)

@then('the string will return with uppercased letters')
def step_impl(context):
    assert (context.uppercased_string == "ASDF")
