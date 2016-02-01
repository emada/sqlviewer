import json
import glob
import os

from tornado.httpclient import AsyncHTTPClient
from vizydrop.sdk.source import SourceFilter
from vizydrop.fields import *


class FileChooserFilter(SourceFilter):
    def get_file_options(account, **kwargs):
        # note that this function will be run as a Tornado coroutine (see gen.coroutine)
        # but does not require the decorator
        # data_dir = os.path.join(os.path.dirname(__file__), '../queries')
        # data_dir = "~/projects/sqlviewer/sqlpad/db/"
        data_dir = os.environ['SQLPAD_PATH']
        files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
        print([{"title": f, "value": f} for f in files])
        return [{"title": f, "value": f} for f in files]

    file = TextField(name="File", description="Name of the flatfile to open", optional=False,
                     get_options=get_file_options)
