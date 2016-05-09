# -*- coding: utf-8 -*-
import os.path

from flask.ext.assets import Environment, Bundle
from flask.ext.collect import Collect


def get_files_for_settings(app, assets_key, from_static=True):
    result = []
    if assets_key in app.config and len(app.config[assets_key]) > 0:
        if from_static:
            result = [
                os.path.join(app.static_folder, static_file)
                for static_file in app.config[assets_key]
                ]
        else:
            result = app.config[assets_key]
    return result


def init(app):
    """
    Bundle projects assets

    :type app: flask.Flask
    """
    assets = Environment(app)
    assets.auto_build = app.config.get('ASSETS_AUTO_BUILD', True)
    files_to_watch = []
    if 'COLLECT_STATIC_ROOT' in app.config:
        assets.cache = app.config['COLLECT_STATIC_ROOT']
        collect = Collect()
        collect.init_app(app)
        collect.collect()
        app.static_folder = app.config['COLLECT_STATIC_ROOT']

    for key in ['js', 'css']:
        assets_key = '%s_ASSETS' % key.upper()
        additional = get_files_for_settings(app,
                                            '%s_ADDITIONAL' % assets_key,
                                            from_static=False)
        files_to_watch.extend(get_files_for_settings(app, assets_key))
        files_to_watch.extend(additional)

        build_files = app.config[assets_key] + additional

        bundle = Bundle(*build_files,
                        output=app.config['%s_OUTPUT' % assets_key],
                        filters=app.config['%s_FILTERS' % assets_key]
                        )

        assets.register('%s_all' % key, bundle)

    app.assets = assets
    app._base_files_to_watch = files_to_watch
