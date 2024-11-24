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


class ComputerType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "Desktop": "DESKTOP",
            "Laptop": "LAPTOP",
            "N/A": "N_A",
            "Domain Controller": "DOMAIN_CONTROLLER",
            "Server": "SERVER",
        }
    
    @schemas.classproperty
    def DESKTOP(cls):
        return cls("Desktop")
    
    @schemas.classproperty
    def LAPTOP(cls):
        return cls("Laptop")
    
    @schemas.classproperty
    def N_A(cls):
        return cls("N/A")
    
    @schemas.classproperty
    def DOMAIN_CONTROLLER(cls):
        return cls("Domain Controller")
    
    @schemas.classproperty
    def SERVER(cls):
        return cls("Server")
