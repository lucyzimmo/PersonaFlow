# encoding=utf8

from wsme.exc import (ClientSideError, InvalidInput, MissingArgument,
                      UnknownArgument)


def test_clientside_error():
    e = ClientSideError("Test")

    assert e.faultstring == "Test"


def test_unicode_clientside_error():
    e = ClientSideError("\u30d5\u30a1\u30b7\u30ea")

    assert e.faultstring == "\u30d5\u30a1\u30b7\u30ea"


def test_invalidinput():
    e = InvalidInput('field', 'badvalue', "error message")

    assert e.faultstring == (
        "Invalid input for field/attribute field. Value: 'badvalue'. "
        "error message"
    ), e.faultstring


def test_missingargument():
    e = MissingArgument('argname', "error message")

    assert e.faultstring == \
        ('Missing argument: "argname": error message'), e.faultstring


def test_unknownargument():
    e = UnknownArgument('argname', "error message")

    assert e.faultstring == \
        ('Unknown argument: "argname": error message'), e.faultstring
