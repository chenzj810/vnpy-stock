# encoding: UTF-8

from vnpy.trader.language import vtConstant
from .windGateway import WindGateway

gatewayClass = WindGateway
gatewayName = 'WIND'
gatewayDisplayName = '万得'
gatewayType = vtConstant.GATEWAYTYPE_DATA
gatewayQryEnabled = False
