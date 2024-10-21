from playwright.async_api import expect, Page

class InvoiceDetailsPage:
    def __init__(self, page):
        self.page = page
        self.invoice_hotel_name_selector = 'h4'
        self.invoice_number_selector = 'h6'
        self.invoice_date_selector = 'section > div > ul > li:nth-child(1)'
        self.due_date_selector = 'section > div > ul > li:nth-child(2)'
        self.booking_code_selector = 'table > tbody > tr:nth-child(1) > td:nth-child(2)'  
        self.room_selector = 'table > tbody > tr:nth-child(2) > td:nth-child(2)'  
        self.total_stay_count_selector = 'table > tbody > tr:nth-child(3) > td:nth-child(2)'
        self.total_stay_amount_selector = 'table > tbody > tr:nth-child(4) > td:nth-child(2)'
        self.check_in_selector = 'table > tbody > tr:nth-child(5) > td:nth-child(2)'
        self.check_out_selector = 'table > tbody > tr:nth-child(6) > td:nth-child(2)'
        self.customer_details_selector = 'section > div > div' 
        self.deposit_now_selector = 'table.table:nth-child(12) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)'
        self.tax_vat_selector = 'table.table:nth-child(12) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)'
        self.total_amount_selector = 'table.table:nth-child(12) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)'

    async def validate_information(self):
        return self.page.get_by_text('Rendezvous Hotel')
    
    async def validate_invoice_details(self, expected_details, page: Page): 
        invoice_number_text = await page.inner_text(self.invoice_number_selector) 
        extracted_invoice_number = invoice_number_text.split("#")[1].split(" ")[0] 
        assert await page.inner_text(self.invoice_hotel_name_selector) == expected_details['HotelName'], "Hotel name does not match."
        assert extracted_invoice_number == expected_details['InvoiceNumber'], "Invoice number does not match." 

        invoice_date_text = await page.inner_text(self.invoice_date_selector)
        extracted_invoice_date = invoice_date_text.split(": ")[1]
        assert extracted_invoice_date == expected_details['InvoiceDate'], "Invoice date does not match."

        due_date_text = await page.inner_text(self.due_date_selector)
        extracted_due_date = due_date_text.split(": ")[1]
        assert extracted_due_date == expected_details['DueDate'], "Due date does not match."

        assert await page.inner_text(self.booking_code_selector) == expected_details['BookingCode'], "Booking code does not match."
        assert await page.inner_text(self.room_selector) == expected_details['Room'], "Room type does not match."
        assert await page.inner_text(self.check_in_selector) == expected_details['CheckIn'], "Check-in date does not match."
        assert await page.inner_text(self.check_out_selector) == expected_details['CheckOut'], "Check-out date does not match."
        
        customer_detail = await page.inner_html(self.customer_details_selector)
        extracted_customer_details = customer_detail.split('<br>')
        customer_detail_name = extracted_customer_details[0].strip()  
        customer_detail_address = extracted_customer_details[1].strip() 
        customer_detail_zip_code = extracted_customer_details[2].strip()  
        assert customer_detail_name == expected_details['CustomerDetailsName'], "Customer Details Name does not match." 
        assert customer_detail_address == expected_details['CustomerDetailsAddress'], "Customer Details Address does not match." 
        assert customer_detail_zip_code == expected_details['CustomerDetailsZipCode'], "Customer Details Zip Code does not match."

        assert await page.inner_text(self.total_stay_count_selector) == expected_details['TotalStayCount'], "Total stay count does not match."
        assert await page.inner_text(self.total_stay_amount_selector) == expected_details['TotalStayAmount'], "Total stay amount does not match."
        assert await page.inner_text(self.deposit_now_selector) == expected_details['DepositNow'], "Deposit Now does not match."
        assert await page.inner_text(self.tax_vat_selector) == expected_details['Tax&VAT'], "Tax&VAT does not match."
        assert await page.inner_text(self.total_amount_selector) == expected_details['TotalAmount'], "Total Amount does not match." 

    async def click_link(self): 
        await self.page.get_by_text("Invoice Details").first.click()
        new_page = await self.page.context.wait_for_event("page")  
        await new_page.wait_for_load_state()
        return new_page



































