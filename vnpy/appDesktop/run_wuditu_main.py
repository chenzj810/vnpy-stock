
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:40:25 2017

@author: chen
在vnpy基础上修改
"""

# encoding: UTF-8

# 重载sys模块，设置默认字符串编码方式为utf8
import sys
from imp import reload
reload(sys)
#sys.setdefaultencoding('utf8')

# vn.trader模块
from vnpy.service.event import EventEngine
from vnpy.service.main.vtEngine import MainEngine
from vnpy.appDesktop.windows.uiQt import qApp
from vnpy.appDesktop.windows.uiMainWindow import MainWindow


# 加载底层接口
from vnpy.service.tradeGateway.gateway import eastMoneyGateway

# 加载上层应用
#from vnpy.service.app import dataRecorder
#from vnpy.service.language import riskManager
#from vnpy.service.language import strategyManager
from vnpy.service.tradeStrategy import strategyAtrRsi
from vnpy.service.tradeStrategy import strategyDualThrust
from vnpy.service.tradeStrategy import strategyMacdShake
from vnpy.service.tradeRiskCtrl import riskCtrl1



#----------------------------------------------------------------------
def main():
    """主程序入口"""

    print("main start")
    # 创建事件引擎
    ee = EventEngine()

    # 创建主引擎
    me = MainEngine(ee)

    # 添加交易接口， 包括行情数据接口和交易接口两部分
    print("添加gateway接口, addGatewayClass")
    me.addGatewayClass(eastMoneyGateway)

    # 添加上层应用, 应用管理
    #me.addApp(strategyManager)

    print("添加上层应用, addRiskCtrlClass")
    me.addRiskCtrlClass(riskCtrl1)

    print("添加上层应用, addStrategyClass")
    me.addStrategyClass(strategyDualThrust)
    me.addStrategyClass(strategyAtrRsi)
    me.addStrategyClass(strategyMacdShake)

    #me.addApp(dataRecorder)
    print("添加上层应用, dataRecorder")

    # 创建主窗口
    mw = MainWindow(me, ee)
    mw.showMaximized()

    # 在主线程中启动Qt事件循环
    qApp.exec_()

    try:
        me.exit()
        sys.exit(0)
    except:
        print('GoodBye!')
        pass


if __name__ == '__main__':
    main()