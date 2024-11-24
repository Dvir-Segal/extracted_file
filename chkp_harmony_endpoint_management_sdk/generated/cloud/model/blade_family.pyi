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


class BladeFamily(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def GENERAL_SETTINGS(cls):
        return cls("General Settings")
    
    @schemas.classproperty
    def THREAT_PREVENTION(cls):
        return cls("Threat Prevention")
    
    @schemas.classproperty
    def DATA_PROTECTION(cls):
        return cls("Data Protection")
    
    @schemas.classproperty
    def ONE_CHECK(cls):
        return cls("OneCheck")
    
    @schemas.classproperty
    def DEPLOYMENT(cls):
        return cls("Deployment")
    
    @schemas.classproperty
    def REMOTE_ACCESS_VPN(cls):
        return cls("Remote Access VPN")
    
    @schemas.classproperty
    def CAPSULE_DOCS(cls):
        return cls("Capsule Docs")
    
    @schemas.classproperty
    def ACCESS(cls):
        return cls("Access")
    
    @schemas.classproperty
    def AGENT_SETTINGS(cls):
        return cls("Agent Settings")
    
    @schemas.classproperty
    def DATA_LOSS_PREVENTION(cls):
        return cls("Data Loss Prevention")
    
    @schemas.classproperty
    def URL_FILTERING_FROM_NETWORK_MANAGEMENT(cls):
        return cls("Url Filtering From Network Management")