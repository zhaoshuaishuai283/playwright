import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://test-login.ke.com/login?service=http%3A%2F%2Ftest1-huiting.ttb.test.ke.com%2Flogin%2Fcas?rurl=http%253A%252F%252Ftest1-huiting.ttb.test.ke.com%252FtaskCenter")
    page.get_by_role("link", name="账号登录").click()
    page.get_by_role("textbox", name="请输入手机号/系统号/账号").click()
    page.get_by_role("textbox", name="请输入手机号/系统号/账号").fill("27151339")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("H0meL1nk")
    page.get_by_role("button", name="登 录").click()
    expect(page.get_by_role("menuitem", name="智能任务中心").locator("span")).to_be_visible()
    page.get_by_role("row", name="UI自动化录制验证 1922838886789533696").locator("span").nth(1).click()
    page.get_by_role("button", name="close-circle").click()
    page.get_by_role("textbox", name="* API Key info-circle ：").click()
    page.get_by_role("textbox", name="* API Key info-circle ：").fill("PPR47yWyKXIxRFLRRiB8XrhgrXOA78BL")
    page.locator("#workflowIframe").content_frame.get_by_text("流程调试").click()
    page.locator("#workflowIframe").content_frame.get_by_role("button", name="开始运行").click()
    expect(page.locator("#workflowIframe").content_frame.get_by_text("流程调试中")).to_be_visible()
    # expect(page.locator("#workflowIframe").content_frame.get_by_text("SUCCESS").first).to_be_visible()
    page.get_by_role("button", name="任务效果调试").click()
    page.get_by_role("button", name="开始调试").click()
    expect(page.get_by_role("alert")).to_contain_text("运行调试中：正在查询数据，预计还需3-5min")
    expect(page.get_by_text("调试完成!点这里查看结果")).to_be_visible()
    page.get_by_role("button", name="发布上线").click()
    expect(page.get_by_text("API Key：PPR47yWyKXIxRFLRRiB8XrhgrXOA78BL")).to_be_visible()
    page.get_by_role("button", name="确认上线").click()
    expect(page.get_by_text("发布成功")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
