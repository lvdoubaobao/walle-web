# -*- coding: utf-8 -*-
"""
    walle-web

    :copyright: © 2015-2017 walle-web.io
    :created time: 2017-06-14 16:00:23
    :author: wushuiyong@walle-web.io
"""
import logging

from flask import jsonify, abort
from flask.ext.login import login_required
from flask.ext.login import current_user
from flask_restful import Resource
from walle.service.rbac.access import Access as AccessRbac
from walle.model.user import load_user

class ApiResource(Resource):
    module = None
    controller = None
    action = None

    @staticmethod
    def render_json(code=0, message='', data=[]):
        return jsonify({
            'code': code,
            'message': message,
            'data': data,
        })

    @staticmethod
    def json(code=0, message=None, data=[]):
        return jsonify({
            'code': code,
            'message': message,
            'data': data,
        })

    @staticmethod
    def list_json(list, count, table={}, code=0, message=''):
        return ApiResource.render_json(data={'list': list, 'count': count, 'table': table},
                                       code=code,
                                       message=message)


class SecurityResource(ApiResource):
    module = None
    controller = None
    action = None

    @login_required
    def get(self, *args, **kwargs):
        self.action = 'get'
        is_allow = AccessRbac.is_allow(action=self.action, controller=self.controller)
        if not is_allow:
            self.render_json(code=403, message=u'无操作权限')
            # abort(403)
            pass
        pass

    @login_required
    def delete(self, *args, **kwargs):
        self.action = 'delete'
        is_allow = AccessRbac.is_allow(action=self.action, controller=self.controller)
        if not is_allow:
            self.render_json(code=403, message=u'无操作权限')
            # abort(403)
            pass
        pass

    @login_required
    def put(self, *args, **kwargs):
        self.action = 'put'
        is_allow = AccessRbac.is_allow(action=self.action, controller=self.controller)
        if not is_allow:
            self.render_json(code=403, message=u'无操作权限')
            # abort(403)
            pass
        pass

    @login_required
    def post(self, *args, **kwargs):
        """
        # @login_required
        :param args:
        :param kwargs:
        :return:
        """
        self.action = 'post'
        is_allow = AccessRbac.is_allow(action=self.action, controller=self.controller)
        if not is_allow:
            self.render_json(code=403, message=u'无操作权限')
            # abort(403)
            pass
        pass



class Base(Resource):
    def get(self):
        """
        fetch role list or one role

        :return:
        """
        return 'walle-web 2.0'
