class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app"
        self.username_selector = 'input[name="username"]'
        self.password_selector = 'input[name="password"]'
        self.login_button_selector = 'button[type="submit"]'
        self.success_element_selector = '.mt-5'  
        self.error_message_selector = '.mt-3'
 
    async def is_login_successful(self):
        await self.page.goto(self.url)
        await self.page.fill(self.username_selector, "demouser")
        await self.page.fill(self.password_selector, 'abc123')
        await self.page.click(self.login_button_selector)
        return await self.page.is_visible(self.success_element_selector)
 
    async def get_username_error_message(self):
        await self.page.goto(self.url)
        await self.page.fill(self.username_selector, "Demouser")
        await self.page.fill(self.password_selector, "abc123")
        await self.page.click(self.login_button_selector)
        return await self.page.inner_text(self.error_message_selector)
   
    async def get_username_and_password_error_message(self):
        await self.page.goto(self.url)
        await self.page.fill(self.username_selector, "demouser_")
        await self.page.fill(self.password_selector, "xyz")
        await self.page.click(self.login_button_selector)
        return await self.page.inner_text(self.error_message_selector)
   
    async def get_password_error_message(self):
        await self.page.goto(self.url)
        await self.page.fill(self.username_selector, "demouser")
        await self.page.fill(self.password_selector, "nananana")
        await self.page.click(self.login_button_selector)
        return await self.page.inner_text(self.error_message_selector)

