from playwright.sync_api import sync_playwright

seeds = [38,39,40,41,42,43,44,45,46,47]
grand_total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_selector("table")

        cells = page.query_selector_all("table td")
        numbers = []

        for cell in cells:
            try:
                num = float(cell.inner_text())
                numbers.append(num)
            except:
                pass

        grand_total += sum(numbers)

    print("FINAL TOTAL:", grand_total)
    browser.close()