#coding=utf-8
# authorized by Saltyric
from pymysql import connect
import time


class JD(object):
    def __init__(self):
        #   创建数据库连接
        self.conn = connect(host="localhost",
                            port=3306,
                            user="root",
                            password="mysql",
                            database="jing_dong",
                            charset="utf8")
        #  获取cursor对象
        self.cs = self.conn.cursor()
        self.acc_check = False
        self.user_id = ""
        self.user = ""
        self.password = ""
        self.addr = ""
        self.tel = ""
        self.current_time = ""

    def __del__(self):
        #   关闭Cursor对象
        self.cs.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cs.execute(sql)
        for temp in self.cs.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有商品"""
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        """显示所有分类"""
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        """显示所有品牌"""
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    def show_orders(self):
        """显示当前用户的已购订单"""
        if self.account_check():
            sql = """select * from orders where customer_id=%s order by id;""" % self.user_id
            print("============已购订单如下==============")
            print("|-单号---------日期----------客户ID--|")
            self.execute_sql(sql)
            print("====================================")
        else:
            print("请先登录！")

    def show_order_detail(self):
        """显示当前用户的订单详情"""
        if self.account_check():
            print("================订单详情================")
            print("|单号-用户ID-------日期-------商品ID-数量-|")
            sql = """select o.id, o.customer_id, o.order_date_time, od.good_id, od.quantity from order_detail 
            as od inner join (select * from orders where customer_id=%s) as o on o.id=od.order_id order by od.id; """ % self.user_id
            self.execute_sql(sql)
            print("=======================================")
        else:
            print("请先登录！")

    def add_brand(self):
        """在当前用户下用户选择添加一个新的的品牌"""
        if self.account_check():
            item_name = input("输入新品牌名称: ")
            sql = """insert into goods_brands (name) values (%s);"""
            confirm = input("确认提交？ y/n ")

            if confirm == "y":
                try:
                    self.cs.execute(sql, [item_name])
                except Exception as result:
                    self.conn.rollback()
                    print("出现错误...")
                else:
                    self.conn.commit()
                    print("添加成功!!")
            else:
                print("已取消添加...")
        else:
            print("请先登录！！")

    def add_item(self):
        """在当前用户下添加物品函数"""
        if self.account_check():
            self.show_all_items()
            self.item_select = input("请选择要选购的物的序号: ")
            sql = """select id,name from goods where id=%s;"""

            try:
                self.cs.execute(sql, [self.item_select])
            except Exception as result:
                print("出现错误: %s" % result)
            else:
                self.temp = self.cs.fetchone()
                print(self.temp)
            
            if self.temp:
                try:
                    self.item_num = int(input("请输入需要的数量: "))
                except Exception as result:
                    print("输入错误！")
                else:
                    self.create_orders(self.temp[0], self.item_num)
            else:
                print("无法找到该商品！")
        else:
            print("请先登录！！")
    
    def create_orders(self, item_id, item_num):
        """创建一个订单，并把参数传递给订单详情函数"""
        print("---->输入的商品序号为: %s<----" % item_id)
        self.current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print("正在创建订单...%s %s" % (self.current_time, item_num))
        item_sql = """insert into orders (order_date_time, customer_id) values (%s,%s);"""

        try:
            self.cs.execute(item_sql, [self.current_time, self.user_id])
        except Exception as result:
            self.conn.rollback()
            print("出现错误: %s" % result)
        else:
            self.conn.commit()
            self.create_order_detail(self.current_time, item_id, item_num)

    def create_order_detail(self, time, item_id, item_num):
        """创建一个订单详情"""
        sql = """select id from orders where order_date_time='%s' and customer_id=%s""" % (time, self.user_id)
        self.cs.execute(sql)
        self.order_id = self.cs.fetchone()

        detail_sql = """insert into order_detail (order_id, good_id, quantity) values (%s,%s,%s);""" % (self.order_id[0], item_id, item_num)
        self.cs.execute(detail_sql)
        self.conn.commit()
        print("创建订单成功！")

    def regist_account(self):
        """用户注册函数"""
        self.user = input("请输入要注册的账号名: ")
        self.password = input("请输入注册密码: ")
        self.addr = input("请输入您的地址: ")
        self.tel = input("请输入您的电话: ")
        sql = """insert into customers (name,address,tel,password) values (%s,%s,%s,%s);"""
        try:
            self.cs.execute(sql, [self.user, self.addr, self.tel, self.password])
        except Exception as result:
            self.conn.rollback()
            print("出现错误: %s" % result)
            return False
        else:
            self.conn.commit()
            self.acc_check = True
            return True

    def account_login(self):
        """用户登录函数"""
        if self.account_check():
            print("...已经登录...")

    def account_check(self):
        """登录验证函数，若未登录，则提醒创建一个用户"""
        if self.acc_check:
            return True
        else:
            self.user = input("请输入用户账号: ")
            self.password = input("请输入密码: ")

            sql = """select id, name from customers where name=%s and password=%s;"""
            if self.cs.execute(sql, [self.user, self.password]) == 1:
                # if self.cs.execute(sql, [self.password]) == 1
                self.acc_check = True
                self.info = self.cs.fetchone()
                self.user_id = self.info[0]
                self.user = self.info[1]
                print("欢迎回来，%s！" % self.user)
                return True
            else:
                print("账户或密码错误！")
                self.regist_call = input("是否进行账号注册？ y/n")
                if self.regist_call == "y":
                    if self.regist_account():
                        return True
                else:
                    self.user = ""
                    return False

    def get_info_by_name(self):
        """商品查询函数"""
        #   防止注入----> ' or 1=1 or '<----得到所有商品数据
        find_name = input("请输入要查询的商品名字: ")
        # sql = """select * from goods where name='%s';""" % find_name
        # print("------>%s<-------" % sql)
        # self.execute_sql(sql)
        sql = "select * from goods where name=%s"
        self.cs.execute(sql, [find_name])
        print(self.cs.fetchall())

    def print_menu(self):
        print("------京东商城------")
        print("------欢迎光临 %s------" % self.user)
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        print("4: 添加一个商品分类")
        print("5: 根据名字查询一个商品")
        print("6: 选择要购买的商品")
        print("7: 查看已购订单")
        print("8: 查看订单详情")
        print("9: 用户登录")
        print("0: 退出")
        return input("请输入功能对应的序号: ")

    def run(self):
        while True:
            option = self.print_menu()
            if option == "1":
                #   查询所有商品
                self.show_all_items()
            elif option == "2":
                #   查询分类
                self.show_cates()
            elif option == "3":
                #   查询品牌分类
                self.show_brands()
            elif option == "4":
                #   添加品牌
                self.add_brand()
            elif option == "5":
                self.get_info_by_name()
            elif option == "6":
                self.add_item()
            elif option == "7":
                self.show_orders()
            elif option == "8":
                self.show_order_detail()
            elif option == "9":
                self.account_login()
            elif option == "0":
                break
            else:
                print("输入有误，请重新输入...")


def main():
    #   创建一个京东商城对象
    jd = JD()

    #   调用这个对象的run方法，让其运行
    jd.run()


if __name__ == "__main__":
    main()
