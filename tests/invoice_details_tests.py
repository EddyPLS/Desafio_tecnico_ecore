import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.Invoice_details_page import InvoiceDetailsPage

class TestInvoiceDetails:
    @pytest.mark.asyncio
    async def test_003_validate_invoice_information_is_presented(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            assert await login_page.is_login_successful()
            invoice_details_page = InvoiceDetailsPage(page)
            assert await invoice_details_page.validate_information()
            print("Validation with success")
            
            new_page = await invoice_details_page.click_link() 
            print("click with success")
            expected_details = {
                'HotelName': 'Rendezvous Hotel',
                'InvoiceNumber': '110',
                'InvoiceDate': '14/01/2018',
                'DueDate': '15/01/2018',
                'BookingCode': '0875',
                'Room': 'Superior Double',
                'CheckIn': '14/01/2018',
                'CheckOut': '15/01/2018',
                'CustomerDetailsName': 'JOHNY SMITH', 
                'CustomerDetailsAddress': 'R2, AVENUE DU MAROC', 
                'CustomerDetailsZipCode': '123456', 
                'TotalStayCount': '1',
                'TotalStayAmount': '$150',
                'DepositNow': 'USD $20.90',
                'Tax&VAT': 'USD $19',
                'TotalAmount': 'USD $209',
            }
            
            await invoice_details_page.validate_invoice_details(expected_details, new_page)  
            await browser.close()


























