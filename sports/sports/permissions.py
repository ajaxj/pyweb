#coding=utf-8
"""
用户权限管理
"""
__author__ = 'window2003@gmail.com'

from flaskext.principal import  RoleNeed,Permission

admin = Permission(RoleNeed('admin'))
moderator = Permission(RoleNeed('moderator'))
#验证角色
auth = Permission(RoleNeed('authenticated'))

# this is assigned when you want to block a permission to all
# never assign this role to anyone !
null = Permission(RoleNeed('null'))
