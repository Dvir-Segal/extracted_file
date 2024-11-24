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


class EntityType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def ORGANIZATION_ROOT(cls):
        return cls("ORGANIZATION_ROOT")
    
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
    def IP_RANGE(cls):
        return cls("IP_RANGE")
    
    @schemas.classproperty
    def GATEWAY(cls):
        return cls("GATEWAY")
    
    @schemas.classproperty
    def OTHER_USERS_AND_COMPUTERS(cls):
        return cls("OTHER_USERS_AND_COMPUTERS")
    
    @schemas.classproperty
    def DIRECTORIES_ROOT(cls):
        return cls("DIRECTORIES_ROOT")
    
    @schemas.classproperty
    def IP_RANGES_ROOT(cls):
        return cls("IP_RANGES_ROOT")
    
    @schemas.classproperty
    def VIRTUAL_GROUPS_ROOT(cls):
        return cls("VIRTUAL_GROUPS_ROOT")
    
    @schemas.classproperty
    def WORKGROUPS_ROOT(cls):
        return cls("WORKGROUPS_ROOT")
    
    @schemas.classproperty
    def DELETED_USERS_AND_COMPUTERS_ROOT(cls):
        return cls("DELETED_USERS_AND_COMPUTERS_ROOT")
    
    @schemas.classproperty
    def DEPLOYMENT_ROOT(cls):
        return cls("DEPLOYMENT_ROOT")
    
    @schemas.classproperty
    def OFFLINE_GROUPS_ROOT(cls):
        return cls("OFFLINE_GROUPS_ROOT")
    
    @schemas.classproperty
    def OFFLINE_GROUP(cls):
        return cls("OFFLINE_GROUP")
    
    @schemas.classproperty
    def DUMMY(cls):
        return cls("DUMMY")
