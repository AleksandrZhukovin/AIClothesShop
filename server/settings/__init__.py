from os import environ

from split_settings.tools import include, optional


# Managing environment via `DJANGO_ENV` variable:
environ.setdefault('DJANGO_ENV', 'development')
_ENV = environ['DJANGO_ENV']

_base_settings = (
    'components/common.py',
    # 'components/static_and_media_files.py',
    # Select the right env:
    # f'environments/{_ENV}.py',
    # Optionally override some settings:
   #  optional('environments/local.py'),
)

# Include settings:
include(*_base_settings)
