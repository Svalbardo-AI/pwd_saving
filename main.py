# coding = utf-8

import functions as F
import os
import configparser

work_path = os.getcwd()


class pws_storage:
    def __init__(self):
        self.config_webs = configparser.ConfigParser()
        self.config_webs.read(work_path + '\\' + 'webs.ini', 'utf-8')
        self.pwd_dict = {}
        for i in range(len(self.config_webs.sections())):
            module_name = self.config_webs.sections()[i]
            module = self.config_webs.items(module_name)
            self.pwd_dict[module_name] = [a[1] for a in module]

        self.config_nicknames = configparser.ConfigParser()
        self.config_nicknames.read(work_path + '\\' + 'nicknames.ini', 'utf-8')

        self._index()

    def _return_to_index(self):
        print('\n按回车键回到首页')
        input()
        F.clear_screen()
        self._index()

    def _index(self):
        print('==========选择功能==========')
        print('\t  1.添加\n\t  2.查找\n\t  3.添加网站\n\t  0.退出')
        print('==========================')
        try:
            choice = int(input())
            self._goto(choice)
        except Exception as e:
            print(e, '\n请输入数字')
            self._return_to_index()

    def _goto(self, target):
        if target == 1:
            F.clear_screen()
            website = str(input('输入网站（建议使用常用网站中文名，如网易、微软、腾讯、美团： '))
            website = F.nick_name(website)
            print('目标网站： ', website)
            self._add_new(website)
        elif target == 2:
            F.clear_screen()
            website = str(input('输入网站（建议使用常用网站中文名，如网易、微软、腾讯、美团： '))
            website = F.nick_name(website)
            print('目标网站： ', website)
            self._search(website)
        elif target == 3:
            F.clear_screen()
            website = str(input('输入网站（建议使用常用网站中文名，如网易、微软、腾讯、美团： '))
            if (website in self.config_nicknames.sections()) == 1:
                print('网址已存在')
                self._return_to_index()
            else:
                self._add_webs(website)
        elif target == 0:
            quit()
        else:
            print('输入错误，请重试。')
            self._index()

    def _add_new(self, website):
        if F.isExist(website, self.pwd_dict) == 0:
            account = str(input('输入账号（手机号、邮箱或用户名）： ')).lower()
            pwd = str(input('输入密码： '))
            pwd = F.lock(pwd)
            self.pwd_dict[website] = (account, pwd)
            self.config_webs.add_section(website)
            self.config_webs.set(website, 'account', account)
            self.config_webs.set(website, 'password', pwd)
            print('已加密保存：', self.pwd_dict[website])
            self.config_webs.write(open(work_path + '\\' + 'webs.ini', 'w'))
            print('\n按回车键回到首页......')
            input()
            F.clear_screen()
            self._index()
        else:
            F.clear_screen()
            print('该网址已有存储的账户和密码')
            self._index()

    def _search(self, website):
        if F.isExist(website, self.pwd_dict) == 1:
            account = self.pwd_dict[website][0]
            pwd = self.pwd_dict[website][1]
            pwd = F.unlock(pwd)
            print('账号： ', account, '\n密码： ', pwd)
            self._return_to_index()
        else:
            print(0)

    def _add_webs(self, website):
        name = str(input('请输入该网站常用名： '))

        self.config_nicknames.add_section(website)
        self.config_nicknames.set(website, 'name', name)
        self.config_nicknames.write(open(work_path + '\\' + 'nicknames.ini', 'w'))
        print('添加完毕。')
        self._return_to_index()


if __name__ == '__main__':
    storage = pws_storage()
