#! /usr/bin/env python

import os
import sys

# Register all available formats
from al_contacts.formats import Formats
from al_contacts.format import JsonFormat, PickleFormat

dataFormats = Formats()
jsonDataFormat = JsonFormat(dataFormats)
pickleDataFormat = PickleFormat(dataFormats)

# generate a map of format names versus format objects
FORMATS_MAP = {}
for fmt in dataFormats.formats:
    FORMATS_MAP[str(fmt)] = fmt

# Register reader/writer with specific formats
from al_contacts.reader_writer import JsonRW, PickleRW
jsonReaderWriter = JsonRW(jsonDataFormat)
pickleReaderWriter = PickleRW(pickleDataFormat)

# generate a map of action names versus actual action names
ACTIONS_MAP = {}
for rw in jsonReaderWriter.actions:
    ACTIONS_MAP[str(rw)] = rw

# get all supported views
from al_contacts.views import Views
from al_contacts.view import TableView, ListView

dataViews = Views([])
tableDataView = TableView(dataViews)
listDataView = ListView(dataViews)

# generate a map of view names versus view objects
VIEWS_MAP = {}
for view in dataViews.views:
    VIEWS_MAP[str(view)] = view

