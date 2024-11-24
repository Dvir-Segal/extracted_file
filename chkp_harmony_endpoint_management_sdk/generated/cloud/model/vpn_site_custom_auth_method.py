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


class VpnSiteCustomAuthMethod(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Authentication methods used in conjunction with VPN Site Custom Login
    """


    class MetaOapg:
        enum_value_to_name = {
            "CERTIFICATE": "CERTIFICATE",
            "P12_CERTIFICATE": "P12_CERTIFICATE",
            "OTHER": "OTHER",
        }
    
    @schemas.classproperty
    def CERTIFICATE(cls):
        return cls("CERTIFICATE")
    
    @schemas.classproperty
    def P12_CERTIFICATE(cls):
        return cls("P12_CERTIFICATE")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("OTHER")
