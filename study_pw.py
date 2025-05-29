from asyncio import timeout

import pytest
from playwright.sync_api import Page, expect

def test_denglu(page: Page):
    page.goto("/admin")
    page.wait_for_timeout(5000) #等待页面加载
    page.locator("input[name='username']").fill("username") #点击定位，输入内容
    page.get_by_text("登录").click() #点击登录按钮
    expect(page.get_by_text("智能任务中心")).to_be_visible() #验证登录成功,断言文本可以被看到
    page.pause() #

    #点击操作
    #page.get_by_text("登录").click(modifiers=['Control']) #右键点击
    #page.get_by_text("登录").click(button="right") #右键点击
    #page.get_by_text("登录").click(click_count=3,delay=1_000) #延迟1秒，点击三次
    #page.get_by_text("登录").click(trial=True) #等待点击
