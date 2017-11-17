# -*- coding: utf-8 -*-

"""Unittest fixtures."""

from __future__ import absolute_import, unicode_literals

import datetime

import fauxfactory
import pytest
from gi.repository import Gtk
from hamster_lib.helpers.config_helpers import HamsterAppDirs
from pytest_factoryboy import register

from hamster_gtk import hamster_gtk

from . import factories

register(factories.CategoryFactory)
register(factories.ActivityFactory)
register(factories.FactFactory)


@pytest.fixture
def file_path(request, faker):
    """Return a file path."""
    return faker.uri_path()


@pytest.fixture
def appdirs(request):
    """Return HamsterAppDirs instance."""
    return HamsterAppDirs('hamster-gtk')


# Instances
@pytest.fixture
def app(request, config):
    """
    Return an ``Application`` fixture.

    Please note: the app has just been started but not activated.
    """
    def monkeypatched_reload_config(self):
        return config
    HamsterGTK = hamster_gtk.HamsterGTK  # NOQA
    HamsterGTK._reload_config = monkeypatched_reload_config
    app = HamsterGTK()
    app._startup(app)
    return app


@pytest.fixture
def main_window(request, app):
    """Return a ``ApplicationWindow`` fixture."""
    return hamster_gtk.MainWindow(app)


@pytest.fixture
def header_bar(request, app):
    """
    Return a HeaderBar instance.

    Note:
        This instance has not been added to any parent window yet!
    """
    return hamster_gtk.HeaderBar(app)


@pytest.fixture
def dummy_window(request):
    """
    Return a generic :class:`Gtk.Window` instance.

    This is useful for tests that do not actually rely on external
    functionality.
    """
    return Gtk.Window()


@pytest.fixture(params=(
    fauxfactory.gen_string('utf8'),
    fauxfactory.gen_string('cjk'),
    fauxfactory.gen_string('latin1'),
    fauxfactory.gen_string('cyrillic'),
))
def word_parametrized(request):
    """Return a string paramized with various different charakter constelations."""
    return request.param


@pytest.fixture
def facts_grouped_by_date(request, fact_factory):
    """Return a dict with facts ordered by date."""
    return {}


@pytest.fixture
def set_of_facts(request, fact_factory):
    """Provide a set of randomized fact instances."""
    return fact_factory.build_batch(5)


@pytest.fixture
def config(request, tmpdir):
    """Return a dict of config keys and values."""
    config = {
        'store': 'sqlalchemy',
        'day_start': datetime.time(5, 30, 0),
        'fact_min_delta': 1,
        'tmpfile_path': str(tmpdir.join('tmpfile.hamster')),
        'db_engine': 'sqlite',
        'db_path': ':memory:',
        'autocomplete_activities_range': 30,
        'autocomplete_split_activity': False,
        'tracking_show_recent_activities': True,
        'tracking_recent_activities_count': 6,
    }
    return config
