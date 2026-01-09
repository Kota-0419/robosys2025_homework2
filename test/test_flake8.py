# SPDX-FileCopyrightText: 2025 Kota Matsura
# SPDX-License-Identifier: BSD-3-Clause

from ament_flake8.main import main_with_errors
import pytest


@pytest.mark.flake8
@pytest.mark.linter
def test_flake8():
    rc, errors = main_with_errors()
    
    filtered_errors = []
    for error in errors:
        if 'sitecustomize.py' in error or 'build/' in error:
            continue
        filtered_errors.append(error)

    if len(filtered_errors) == 0:
        return

    assert rc == 0, \
        'Found %d code style errors / warnings:\n' % len(filtered_errors) + \
        '\n'.join(filtered_errors)
