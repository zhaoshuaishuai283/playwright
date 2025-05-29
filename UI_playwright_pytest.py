from asyncio import timeout

import pytest
from playwright.sync_api import Page, expect


#登陆调试平台验证数据权限管理
def test_login_insight(page: Page) -> None:
    page.goto("https://test-login.ke.com/login?service=http%3A%2F%2Ftest1-huiting.ttb.test.ke.com%2Flogin%2Fcas?rurl=http%253A%252F%252Ftest1-huiting.ttb.test.ke.com%252FtaskCenter")
    page.get_by_role("link", name="账号登录").click()
    page.get_by_role("textbox", name="请输入手机号/系统号/账号").click()
    page.get_by_role("textbox", name="请输入手机号/系统号/账号").fill("username")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("password")
    page.get_by_role("button", name="登 录").click()
    expect(page.get_by_role("menuitem", name="智能任务中心").locator("span")).to_be_visible()

    page.get_by_text("数据权限管理").click()
    page.get_by_role("tab", name="我的数据").click()
    expect(page.get_by_role("cell", name="SSC400", exact=True)).to_be_visible()
    page.get_by_role("cell", name="ssc400默认类型").click()


#验证调试上线流程
def test_debug_offline(page: Page) -> None:
    page.goto(
        "https://test-login.ke.com/login?service=http%3A%2F%2Ftest1-huiting.ttb.test.ke.com%2Flogin%2Fcas?rurl=http%253A%252F%252Ftest1-huiting.ttb.test.ke.com%252FtaskCenter")
    page.get_by_role("link", name="账号登录").click()
    page.get_by_role("textbox", name="请输入手机号/系统号/账号").click()
    page.get_by_role("textbox", name="请输入手机号/系统号/账号").fill("username")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("password")
    page.get_by_role("button", name="登 录").click()
    expect(page.get_by_role("menuitem", name="智能任务中心").locator("span")).to_be_visible()

    page.get_by_role("row", name="呃呃呃 1922113819667234816").locator("span").nth(1).click()
    page.locator("#workflowIframe").content_frame.get_by_text("流程调试").click()
    page.locator("#workflowIframe").content_frame.get_by_role("button", name="开始运行").click()
    expect(page.locator("#workflowIframe").content_frame.get_by_text("流程调试中")).to_be_visible()
    expect(page.locator("#workflowIframe").content_frame.locator("body")).to_match_aria_snapshot("- heading \"操作成功\" [level=3]",timeout=30000)

    page.get_by_role("button", name="任务效果调试").click()
    page.get_by_role("spinbutton", name="* 调试数据量(不超过100条)：").click()
    page.get_by_role("spinbutton", name="* 调试数据量(不超过100条)：").fill("5")
    page.get_by_role("button", name="开始调试").click()
    expect(page.get_by_text("取消调试")).to_be_visible()
    expect(page.get_by_role("alert")).to_contain_text("调试完成!点这里查看结果", timeout=60000)
    page.get_by_role("button", name="发布上线").click()
    page.get_by_role("button", name="确认上线").click()
    expect(page.get_by_text("发布成功")).to_be_visible()
