
from playwright.async_api import expect

class InvoiceDetailsPage:
    def __init__(self, page):
        self.page = page
        self.information_selector = 'p2'
        self.invoice_hotel_name_selector = 'h4'
        self.invoice_number_selector = 'h6'
        self.invoice_date_selector = '.div.invoice-date'
        self.due_date_selector = '.div.due-date'
        self.booking_code_selector = 'div.booking-code'  
        self.room_selector = 'div.room'  
        self.total_stay_amount_selector = 'div.total-amount'   
        self.check_in_selector = 'div.check-in'
        self.check_out_selector = 'div.check-out'
        self.customer_details_selector = 'h5'
        self.total_stay_count_selector = 'div.total-count'



    async def validate_information(self):
        return self.page.get_by_text(self.information_selector)
    
    async def validate_invoice_details(self, expected_details):    
        assert await self.page.inner_text(self.invoice_hotel_name_selector) == expected_details['hotel_name'], "Hotel name does not match."
        assert await self.page.inner_text(self.invoice_number_selector) == expected_details['invoice_number'], "Invoice number does not match."
        assert await self.page.inner_text(self.invoice_date_selector) == expected_details['invoice_date'], "Invoice date does not match."
        assert await self.page.inner_text(self.due_date_selector) == expected_details['due_date'], "Due date does not match."
        assert await self.page.inner_text(self.booking_code_selector) == expected_details['booking_code'], "Booking code does not match."
        assert await self.page.inner_text(self.room_selector) == expected_details['room'], "Room type does not match."
        assert await self.page.inner_text(self.total_stay_amount_selector) == expected_details['total_stay_amount'], "Total stay amount does not match."
        assert await self.page.inner_text(self.check_in_selector) == expected_details['check_in'], "Check-in date does not match."
        assert await self.page.inner_text(self.check_out_selector) == expected_details['check_out'], "Check-out date does not match."
        assert await self.page.inner_text(self.customer_details_selector) == expected_details['customer details'], "Customer Details does not match."
        assert await self.page.inner_text(self.total_stay_count_selector) == expected_details['total_stay_count'], "Total stay count does not match."
        
    

    async def click_link(self): 
            await self.page.get_by_text("Invoice Details").first.click()
