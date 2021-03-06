import os
from pathlib import Path
from flask_assets import Environment, Bundle
from webassets.filter import get_filter


class PreBuilder():
    def __init__(self, app):
        self.assets = Environment(app)

        # build
        self.build_js()
        self.build_sass()

    def build_js(self):
        """
        templates 폴더 밑의 모든 js 파일을 번들링하여 static/js로 추출

        [babel setting]
        - install babel-cli globally : `npm install -g babel-cli`
        - install babel-preset-env locally : `npm install --save babel-preset-env`
        """
        print('🏗️ build javascript')

        # get templates path
        dir_path = os.path.dirname(os.path.realpath(__file__))
        templates_path = Path(dir_path).joinpath('templates')

        babel = get_filter('babel', presets='babel-preset-env')
        for js in templates_path.rglob('*.js'):
            js_asset = self.assets.register(js.name, Bundle(
                str(js),
                output=f'js/{js.stem}.min.js',
                filters=[babel, 'rjsmin']
            ))
            js_asset.build()


    def build_sass(self):
        print('🏗️ build sass')
