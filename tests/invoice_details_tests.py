import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.Invoice_details_page import InvoiceDetailsPage
import time

class TestInvoiceDetails:
    @pytest.mark.asyncio
    async def test_01_validate_invoice_information_is_presented(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            login_page = LoginPage(page)
            assert await login_page.is_login_successful()
            invoice_details_page = InvoiceDetailsPage(page)
            assert await invoice_details_page.validate_information()
            print("Validation with success")
            await invoice_details_page.click_link()
            print("click with success")
            expected_details = {
                'hotel_name': 'Rendezvous Hotel',
                'invoice_number': 'Invoice #110 details',
                'invoice_date': 'Invoice Date: 14/01/2018',
                'due_date': 'Due Date: 15/01/2018',
                'booking_code': 'Booking Code 0875',
                'room': 'Room Superior Double',
                'total_stay_amount': 'Total Stay Amount $150',
                'check_in': 'Check-In 14/01/2018',
                'check_out': 'Check-Out 15/01/2018',
                'customer_details': 'Customer Details JOHNY SMITH, R2, AVENUE DU MAROC, 123456',
                'total_stay_count': 'Total Stay count 1',}
            
            await invoice_details_page.validate_invoice_details(expected_details)
            await browser.close()

            
