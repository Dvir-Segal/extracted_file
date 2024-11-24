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


class SearchableEntityTypes(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "GROUP": "GROUP",
            "VIRTUAL_GROUP": "VIRTUAL_GROUP",
            "USER": "USER",
            "COMPUTER": "COMPUTER",
            "OFFLINE_GROUP": "OFFLINE_GROUP",
        }
    
    @schemas.classproperty
    def GROUP(cls):
        return cls("GROUP")
    
    @schemas.classproperty
    def VIRTUAL_GROUP(cls):
        return cls("VIRTUAL_GROUP")
    
    @schemas.classproperty
    def USER(cls):
        return cls("USER")
    
    @schemas.classproperty
    def COMPUTER(cls):
        return cls("COMPUTER")
    
    @schemas.classproperty
    def OFFLINE_GROUP(cls):
        return cls("OFFLINE_GROUP")
