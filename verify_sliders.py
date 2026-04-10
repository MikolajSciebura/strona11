import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://localhost:8081')

        # Scroll to "OSTATNIE REALIZACJE"
        await page.locator('text=OSTATNIE REALIZACJE').scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        await page.screenshot(path='/home/jules/verification/slider_buys_desktop.png')

        # Scroll to "OPINIE"
        await page.locator('text=CO MÓWIĄ O NAS').scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        await page.screenshot(path='/home/jules/verification/slider_opinions_desktop.png')

        # Mobile view
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.goto('http://localhost:8081')

        await page.locator('text=OSTATNIE REALIZACJE').scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        await page.screenshot(path='/home/jules/verification/slider_buys_mobile.png')

        await page.locator('text=CO MÓWIĄ O NAS').scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        await page.screenshot(path='/home/jules/verification/slider_opinions_mobile.png')

        await browser.close()

asyncio.run(run())
