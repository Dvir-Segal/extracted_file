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


class RemediationMode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "NEVER": "NEVER",
            "MEDIUM_HIGH": "MEDIUM_HIGH",
            "HIGH": "HIGH",
            "ALWAYS": "ALWAYS",
        }
    
    @schemas.classproperty
    def NEVER(cls):
        return cls("NEVER")
    
    @schemas.classproperty
    def MEDIUM_HIGH(cls):
        return cls("MEDIUM_HIGH")
    
    @schemas.classproperty
    def HIGH(cls):
        return cls("HIGH")
    
    @schemas.classproperty
    def ALWAYS(cls):
        return cls("ALWAYS")
