# SPDX-FileCopyrightText: 2025 Kota Matsura
# SPDX-License-Identifier: BSD-3-Clause

from ament_flake8.main import main_with_errors
import pytest


@pytest.mark.flake8
@pytest.mark.linter
def test_flake8():
    args = [
        '--max-line-length', '120',
        '--exclude', 'build,lib,.git,__pycache__,.venv'
    ]

    rc, errors = main_with_errors(argv=args)
    assert rc == 0, \
        'Found %d code style errors / warnings:\n' % len(errors) + \
        '\n'.join(errors)
