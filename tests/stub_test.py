#!/usr/bin/env python3

from msfvenomgui import stub

import pytest

def test_stub_sum():
    assert stub.sum(2, 2) == 4
