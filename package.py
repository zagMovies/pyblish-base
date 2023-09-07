# -*- coding: utf-8 -*-

name = 'pyblish_base'

version = '1.8.11.zag'

description = \
    """
    Plug-in driven automation framework for content
    """

authors = ['Abstract Factory and Contributors marcus@abstractfactory.io']

tools = ['pyblish']


# WARNING
# Default plugins that were originally included have been relocated to {root}/pyblish/legacy_plugins

def commands():
    env.PYTHONPATH.append('{root}')
    # env.PATH.append('{root}/bin')

help = [['Home Page', 'https://github.com/pyblish/pyblish']]
