"""Scaffold-level tests confirming the package installs and imports cleanly."""

import opensmartrouting
from opensmartrouting.cli import main


def test_package_has_version() -> None:
    assert opensmartrouting.__version__ == "0.0.1"


def test_cli_main_runs(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert "opensmartrouting" in captured.out
