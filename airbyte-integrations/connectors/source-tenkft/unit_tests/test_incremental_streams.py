#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from airbyte_cdk.models import SyncMode
from pytest import fixture
from source_tenkft.streams import TenkftStream


@fixture
def patch_incremental_base_class(mocker):
    # Mock abstract methods to enable instantiating abstract class
    mocker.patch.object(TenkftStream, "path", "v0/example_endpoint")
    mocker.patch.object(TenkftStream, "primary_key", "test_primary_key")
    mocker.patch.object(TenkftStream, "__abstractmethods__", set())


def test_cursor_field(patch_incremental_base_class):
    stream = TenkftStream("start_date", "end_date", "query")
    expected_cursor_field = []
    assert stream.cursor_field == expected_cursor_field


def test_get_updated_state(patch_incremental_base_class):
    stream = TenkftStream("start_date", "end_date", "query")
    inputs = {"current_stream_state": None, "latest_record": None}
    expected_state = {}
    assert stream.get_updated_state(**inputs) == expected_state


def test_stream_slices(patch_incremental_base_class):
    stream = TenkftStream("start_date", "end_date", "query")
    inputs = {"sync_mode": SyncMode.incremental, "cursor_field": [], "stream_state": {}}
    expected_stream_slice = [None]
    assert stream.stream_slices(**inputs) == expected_stream_slice


def test_supports_incremental(patch_incremental_base_class, mocker):
    mocker.patch.object(TenkftStream, "cursor_field", "dummy_field")
    stream = TenkftStream("start_date", "end_date", "query")
    assert stream.supports_incremental


def test_source_defined_cursor(patch_incremental_base_class):
    stream = TenkftStream("start_date", "end_date", "query")
    assert stream.source_defined_cursor


def test_stream_checkpoint_interval(patch_incremental_base_class):
    stream = TenkftStream("start_date", "end_date", "query")
    expected_checkpoint_interval = None
    assert stream.state_checkpoint_interval == expected_checkpoint_interval
