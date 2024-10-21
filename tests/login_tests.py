import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
 
class TestLogin:
    @pytest.mark.asyncio
    async def test_001_login_positive(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            assert await login_page.is_login_successful()
            print ("Success for Login Positive test")
            await browser.close()
 
    @pytest.mark.asyncio
    async def test_002_interaction1_username_invalid(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            error_message = await login_page.get_username_error_message()
            assert error_message == "Wrong username or password."
            print ("Success for Login Negative username invalid test")
            await browser.close()
 
    @pytest.mark.asyncio
    async def test_002_interaction2_username_and_password_invalid(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            error_message = await login_page.get_username_and_password_error_message()
            assert error_message == "Wrong username or password."
            print ("Success for Login Negative username invalid test")
            await browser.close()
 
    @pytest.mark.asyncio
    async def test_002_interaction3_password_invalid(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            error_message = await login_page.get_password_error_message()
            assert error_message == "Wrong username or password."
            print ("Success for Login Negative username invalid test")
            await browser.close()
 
    @pytest.mark.asyncio
    async def test_002_interaction4_login_positive(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            assert await login_page.is_login_successful()
            print ("Success for Login Positive test")
            await browser.close()