import simplejson
import psycopg2
from psycopg2.extras import RealDictCursor

from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado import gen

from vizydrop.sdk.source import DataSource
from .filter import FileChooserFilter
from .schema import PostgresSchema
import os


class PostgresSource(DataSource):
    class Meta:
        identifier = "sql_file"
        name = "SQL File Name"
        tags = ["sql_file", ]
        description = "Name of the desired SQL query file created using Sqlpad"
        filter = FileChooserFilter

    class Schema(PostgresSchema):
        pass

    @classmethod
    @gen.coroutine
    def get_data(cls, account, source_filter, limit=100, skip=0):
        # conn_string = "host='localhost' dbname='atena_dev' user='ema' password=''"

        sqlpad_path = os.environ['SQLPAD_PATH']
        sqlpad_queries = "queries.db"
        sqlpad_connections = "connections.db"
        filename = sqlpad_path + sqlpad_connections
        with open(filename) as f:
          content = f.readlines()

        d = []
        for c in content:
          data = simplejson.loads(c)
          if data['name'] == 'athena':
            d = data
            break

        if d:
          # conn_string = "host='{0}' dbname='{1}' user='{2}' password='{3}'".format(d['host'], d['database'], d['username'], d['password'])
          conn_string = "host='{0}' dbname='{1}' user='' password=''".format(d['host'], d['database'])

        conn = psycopg2.connect(conn_string)
        cur  = conn.cursor(cursor_factory=RealDictCursor)


        # source_filter = FileChooserFilter(source_filter)
        # if source_filter.file is None:
        #     raise ValueError('required parameter file missing')

        # file_path = os.path.join(os.path.dirname(__file__), '../queries', source_filter.file)
        # if not os.path.isfile(file_path):
        #     raise ValueError('item at path {} is not a file'.format(file_path))

        # with open(file_path, 'rb') as file:
        #     query = file.read()

        filename = sqlpad_path + sqlpad_queries
        with open(filename) as f:
          content = f.readlines()

        query = []
        for c in content:
          data = simplejson.loads(c)
          if data['name'] == source_filter.file:
            query = data['queryText']

        cur.execute(query)
        results = simplejson.dumps(cur.fetchall(), indent=2)
        
        return results


