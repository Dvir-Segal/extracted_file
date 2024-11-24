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


class FreeSearchFilterType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "STARTS_WITH": "STARTS_WITH",
            "EXACT": "EXACT",
            "CONTAINS": "CONTAINS",
            "ENDS_WITH": "ENDS_WITH",
        }
    
    @schemas.classproperty
    def STARTS_WITH(cls):
        return cls("STARTS_WITH")
    
    @schemas.classproperty
    def EXACT(cls):
        return cls("EXACT")
    
    @schemas.classproperty
    def CONTAINS(cls):
        return cls("CONTAINS")
    
    @schemas.classproperty
    def ENDS_WITH(cls):
        return cls("ENDS_WITH")