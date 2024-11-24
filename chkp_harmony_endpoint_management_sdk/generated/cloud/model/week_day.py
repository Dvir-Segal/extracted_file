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


class WeekDay(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "SUNDAY": "SUNDAY",
            "MONDAY": "MONDAY",
            "TUESDAY": "TUESDAY",
            "WEDNESDAY": "WEDNESDAY",
            "THURSDAY": "THURSDAY",
            "FRIDAY": "FRIDAY",
            "SATURDAY": "SATURDAY",
        }
    
    @schemas.classproperty
    def SUNDAY(cls):
        return cls("SUNDAY")
    
    @schemas.classproperty
    def MONDAY(cls):
        return cls("MONDAY")
    
    @schemas.classproperty
    def TUESDAY(cls):
        return cls("TUESDAY")
    
    @schemas.classproperty
    def WEDNESDAY(cls):
        return cls("WEDNESDAY")
    
    @schemas.classproperty
    def THURSDAY(cls):
        return cls("THURSDAY")
    
    @schemas.classproperty
    def FRIDAY(cls):
        return cls("FRIDAY")
    
    @schemas.classproperty
    def SATURDAY(cls):
        return cls("SATURDAY")
