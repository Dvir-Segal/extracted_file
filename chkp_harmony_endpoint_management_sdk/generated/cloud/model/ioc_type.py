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


class IocType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "Domain": "DOMAIN",
            "IP": "IP",
            "URL": "URL",
            "MD5": "MD5",
            "SHA1": "SHA1",
        }
    
    @schemas.classproperty
    def DOMAIN(cls):
        return cls("Domain")
    
    @schemas.classproperty
    def IP(cls):
        return cls("IP")
    
    @schemas.classproperty
    def URL(cls):
        return cls("URL")
    
    @schemas.classproperty
    def MD5(cls):
        return cls("MD5")
    
    @schemas.classproperty
    def SHA1(cls):
        return cls("SHA1")
