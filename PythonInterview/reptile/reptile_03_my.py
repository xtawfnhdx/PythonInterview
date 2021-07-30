"""
模拟淘宝登录
"""
import time
from pynput.mouse import Button, Controller
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image

loginUrl = 'https://login.taobao.com/member/login.jhtml'


def login(username, password):
    '''
    模拟登录淘宝账户
    :param username:用户名
    :param password: 密码
    :return:
    '''
    options = webdriver.ChromeOptions()
    # 设置为开发者模式
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    bro = webdriver.Chrome(options=options)
    bro.maximize_window()

    bro.get(loginUrl)
    time.sleep(1)

    bro.find_element_by_id('fm-login-id').send_keys(username)
    passwordtxt = bro.find_element_by_name('fm-login-password')
    passwordtxt.send_keys(password)

    print(passwordtxt.location.get("x"), passwordtxt.location.get("y"))
    time.sleep(5)




    hua=bro.find_element_by_xpath("//*[@id='nc_1__scale_text']/span")
    print('滑块：', hua.is_enabled())

    action = ActionChains(bro)
    action.click_and_hold(hua)
    action.move_by_offset(245, 0).perform()
    #
    #
    # action.move_to_element_with_offset(passwordtxt, 25, -80)
    # action.click_and_hold()
    # action.move_by_offset(200, 0)
    # action.perform()
    # action.release()
    time.sleep(10)

    # Action(bro)


def Action(bro):
    code_img_ele = bro.find_element_by_xpath("//*[@id='nc_1__scale_text']/span")
    password = bro.find_element_by_xpath("//div/label/i[@class='icon-pwd iconfont']")
    try:
        if code_img_ele:
            mouse = Controller()
            action = ActionChains(bro)
            print(f"当前鼠标位置: {mouse.position}")
            action.move_to_element(password).perform()
            print(f"当前鼠标位置: {mouse.position}")
            action.move_by_offset(-60, 0).perform()
            print(f"当前鼠标位置: {mouse.position}")
            action.context_click()
            action.context_click()
            action.context_click()
            action.context_click()
            time.sleep(1000)
            # 长按且点击
            action.click_and_hold()
            # print("Element is visible? " + str(code_img_ele.is_displayed()))
            # move_by_offset(x,y) x水平方向,y竖直方向
            # perform()让动作链立即执行

            action.move_by_offset(245, 0).perform()
            time.sleep(10)

            # 释放动作链
            action.release()
        else:
            # 登录
            bro.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()
            time.sleep(10)
            i = 100
            bro.quit()  # 关闭浏览器
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # username = input('输入用户名：')
    # password = input('输入密码')
    # login(username, password)

    login('xtawfnhdx', 'weilong.001')
