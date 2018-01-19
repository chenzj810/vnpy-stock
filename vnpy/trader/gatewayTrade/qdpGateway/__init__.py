# encoding: UTF-8

from vnpy.trader.language import vtConstant
from .qdpGateway import QdpGateway

gatewayClass = QdpGateway
gatewayName = 'QDP'
gatewayDisplayName = gatewayName
gatewayType = vtConstant.GATEWAYTYPE_FUTURES
gatewayQryEnabled = True
