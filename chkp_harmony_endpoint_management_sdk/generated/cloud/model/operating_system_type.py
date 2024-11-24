# coding: utf-8

# GTO-MO-1-1 - Removed partial_header
# flake8: noqa

from datetime import date, datetime
import decimal
import functools
import io
import re
import typing
import typing_extensions
import uuid

import frozendict

from chkp_harmony_endpoint_management_sdk.generated.cloud import schemas


class OperatingSystemType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "UNKNOWN": "UNKNOWN",
            "SERVER": "SERVER",
            "MAC_SERVER": "MAC_SERVER",
            "WORKSTATION": "WORKSTATION",
            "LINUX_WORKSTATION": "LINUX_WORKSTATION",
            "MAC_WORKSTATION": "MAC_WORKSTATION",
            "CHROMEOS_WORKSTATION": "CHROMEOS_WORKSTATION",
        }
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("UNKNOWN")
    
    @schemas.classproperty
    def SERVER(cls):
        return cls("SERVER")
    
    @schemas.classproperty
    def MAC_SERVER(cls):
        return cls("MAC_SERVER")
    
    @schemas.classproperty
    def WORKSTATION(cls):
        return cls("WORKSTATION")
    
    @schemas.classproperty
    def LINUX_WORKSTATION(cls):
        return cls("LINUX_WORKSTATION")
    
    @schemas.classproperty
    def MAC_WORKSTATION(cls):
        return cls("MAC_WORKSTATION")
    
    @schemas.classproperty
    def CHROMEOS_WORKSTATION(cls):
        return cls("CHROMEOS_WORKSTATION")
