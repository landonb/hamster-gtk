# -*- coding: utf-8 -*-

"""Fixtures for unittesting the preferences submodule."""

from __future__ import absolute_import, unicode_literals

import datetime

import fauxfactory
import pytest

from hamster_gtk.preferences.preferences_dialog import PreferencesDialog


# Data
@pytest.fixture(params=('sqlalchemy',))
def store_parametrized(request):
    """Return a parametrized store value."""
    return request.param


@pytest.fixture(params=(
    datetime.time(0, 0, 0),
    datetime.time(5, 30, 0),
    datetime.time(17, 22, 0),
))
def day_start_parametrized(request):
    """Return a parametrized day_start value."""
    return request.param


@pytest.fixture(params=(0, 1, 30, 60))
def fact_min_delta_parametrized(request):
    """Return a parametrized fact_min_delta value."""
    return request.param


@pytest.fixture(params=(
    # fauxfactory.gen_utf8(),
    # fauxfactory.gen_latin1(),
    fauxfactory.gen_alphanumeric(),
))
def tmpfile_path_parametrized(request, tmpdir):
    """Return a parametrized tmpfile_path value."""
    return tmpdir.mkdir(request.param).join('tmpfile.hamster')


@pytest.fixture(params=(
    'sqlite',
))
def db_engine_parametrized(request):
    """Return a parametrized db_engine value."""
    return request.param


@pytest.fixture(params=(
    # fauxfactory.gen_utf8(),
    # fauxfactory.gen_latin1(),
    fauxfactory.gen_alphanumeric(),
    ':memory:',
))
def db_path_parametrized(request, tmpdir):
    """Return a parametrized db_path value."""
    if not request.param == ':memory:':
        path = tmpdir.mkdir(request.param).join('hamster.file')
    else:
        path = request.param
    return path


@pytest.fixture(params=(0, 1, 30, 60))
def autocomplete_activities_range_parametrized(request):
    """Return a parametrized autocomplete_activities_range value."""
    return request.param


@pytest.fixture(params=(True, False))
def autocomplete_split_activity_parametrized(request):
    """Return a parametrized autocomplete_split_activity value."""
    return request.param


@pytest.fixture(params=(True, False))
def tracking_show_recent_activities_parametrized(request):
    """Return a parametrized tracking_show_recent_activities_parametrized value."""
    return request.param


@pytest.fixture(params=(0, 1, 5, 15))
def tracking_recent_activities_count_parametrized(request):
    """Return a parametrized tracking_recent_activities_items_parametrized value."""
    return request.param


@pytest.fixture
def config_parametrized(request, store_parametrized, day_start_parametrized,
        fact_min_delta_parametrized, tmpfile_path_parametrized, db_engine_parametrized,
        db_path_parametrized, autocomplete_activities_range_parametrized,
        autocomplete_split_activity_parametrized, tracking_show_recent_activities_parametrized,
        tracking_recent_activities_count_parametrized):
            """Return a config fixture with heavily parametrized config values."""
            return {
                'store': store_parametrized,
                'day_start': day_start_parametrized,
                'fact_min_delta': fact_min_delta_parametrized,
                'tmpfile_path': tmpfile_path_parametrized,
                'db_engine': db_engine_parametrized,
                'db_path': db_path_parametrized,
                'autocomplete_activities_range': autocomplete_activities_range_parametrized,
                'autocomplete_split_activity': autocomplete_split_activity_parametrized,
                'tracking_show_recent_activities': tracking_show_recent_activities_parametrized,
                'tracking_recent_activities_count': tracking_recent_activities_count_parametrized,
            }


# Instances
@pytest.fixture
def preferences_dialog(request, dummy_window, app, config):
    """Return a ``PreferenceDialog`` instance."""
    return PreferencesDialog(dummy_window, app, config)
