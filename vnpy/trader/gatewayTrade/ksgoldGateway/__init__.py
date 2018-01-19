# encoding: UTF-8

from vnpy.trader.language import vtConstant
from .ksgoldGateway import KsgoldGateway

gatewayClass = KsgoldGateway
gatewayName = 'KSGOLD'
gatewayDisplayName = '金仕达黄金'
gatewayType = vtConstant.GATEWAYTYPE_FUTURES
gatewayQryEnabled = True