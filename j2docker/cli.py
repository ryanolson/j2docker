# -*- coding: utf-8 -*-
import click
import yaml

import j2docker


@click.command()
@click.option('--base-image', envvar=["J2D_BASE_IMAGE", "BASE_IMAGE"])
@click.option('--params', type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument('template_file')
def main(template_file, base_image=None, params=None):
    """Console script for j2docker"""
    click.echo("Replace this message by putting your code into "
               "j2docker.cli.main")

    if params:
        with open(params, "r") as stream:
            try:
                params = yaml.load(stream)
            except yaml.YAMLError as exc:
                click.echo(exc)
    with open("Dockerfile", "w") as output:
        output.write(j2docker.render(base_image, template_file, data=params))

if __name__ == "__main__":
    main()
