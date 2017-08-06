""" Airtable Python Wrapper """

import json

class Record(dict):

    def __init__(self, *arg, **kwargs):
        super(Record, self).__init__(*arg, **kwargs)

    @classmethod
    def decode(cls, json_string):
        json_data = json.loads(json_string)
        return cls(json_data)

    def __repr__(self):
        return '<Record: {}>'.format(self.keys())

class Records(list):
    pass

    def __init__(self, iterable=None):
        iterable = iterable or []
        items = [item if isinstance(item, Record) else item for item in iterable]
        super(Records, self).__init__()
        self.extend(items)


    def insert(self, index, value):
        record = value if isinstance(value, Record) else Record(value)
        return super(Records, self).insert(index, record)

    def __repr__(self):
        return '<Records: {}>'.format(len(self))

    # @classmethod
    # def from_response(cls, response=None):
    #     records = Records()
    #     records.extend(response.json().get('records', []))
    #     return records

    # def __len__(self):
    #     return super(Records, self).__len__()
    #
    # def __getitem__(self, i):
    #     return super(Records, self).__getitem__(i)
    #
    # def __delitem__(self, i):
    #     return super(Records, self).__delitem__(i)
    #
    # def __setitem__(self, i, v):
    #     return super(Records, self).__setitem__(i, v)
    #

    #
    # def append(self, item):
    #     record = item if isinstance(item, Record) else Record(item)
    #     return super(Records, self).append(record)
    #
    # def extend(self, iterable):
    #     iterable = [item if isinstance(item, Record) else item for item in iterable]
    #     return super(Records, self).extend(iterable)

    # def __str__(self):
    #     return str(self.list)
