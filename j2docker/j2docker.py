# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, FileSystemLoader, Template

__DEFAULT_BASE_IMAGE__ = "ubuntu:16.04"

base = Template(u"""FROM {{ base_image }}
{{ docker_string }}""")


def render(base_image, template_path, data=None, extensions=None, strict=False):
    data = data or {}
    extensions = extensions or []
    env = Environment(
        loader=FileSystemLoader(os.path.dirname(template_path)),
        extensions=extensions,
        keep_trailing_newline=True,
    )
    if strict:
        from jinja2 import StrictUndefined
        env.undefined = StrictUndefined

    # Add environ global
    env.globals['environ'] = os.environ.get

    output = env.get_template(os.path.basename(template_path)).render(data)
    base_image = base_image or data.get("base_image", __DEFAULT_BASE_IMAGE__)
    docker = base.render(base_image=base_image, docker_string=output.encode('utf-8'))
    return docker.encode('utf-8')
