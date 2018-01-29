# encoding: UTF-8

from vnpy.trader.language import vtConstant
from .cshshlpGateway import CshshlpGateway

gatewayClass = CshshlpGateway
gatewayName = 'CSHSHLP'
gatewayDisplayName = '中信期权'
gatewayType = vtConstant.GATEWAYTYPE_EQUITY
gatewayQryEnabled = True
