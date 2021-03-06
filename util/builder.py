import os
from pathlib import Path
from flask_assets import Environment, Bundle
from webassets.filter import get_filter


class PreBuilder:
    def __init__(self, app, debug=False):
        self.assets = Environment(app)
        self.assets.url = app.static_url_path
        self.assets.debug = debug

        # path
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.templates_path = Path(self.current_path).parent.joinpath('templates')

        # build
        self.build_js()
        self.build_sass()

    def build_js(self):
        """
        js -> babel -> minify -> (later) uglify

        [babel setting]
        - install babel-cli globally : `npm install -g babel-cli`
        - install babel-preset-env locally : `npm install --save babel-preset-env`
        """
        babel = get_filter('babel', presets='babel-preset-env')
        for js in self.templates_path.rglob('*.js'):
            print(js)
            self.assets.register(js.name, Bundle(
                str(js),
                output=f'gen/js/{js.stem}.min.js',
                filters=[babel, 'rjsmin']
            ))

    def build_sass(self):
        """
        scss -> css -> minify -> (later) uglify
        """
        for scss in self.templates_path.rglob('*.scss'):
            print(scss)
            self.assets.register(scss.name, Bundle(
                str(scss),
                filters=['pyscss', 'cssmin'],
                output=f'gen/css/{scss.stem}.min.css'
            ))

