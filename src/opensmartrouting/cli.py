"""Placeholder CLI entry point for OpenSmartRouting.

This is intentionally minimal for Phase 0 (DevOps setup only). The real
routing CLI behavior (accepting stops, geocoding, computing a route, and
producing output) is built in Phase 3 (Python MVP), not here.
"""

from opensmartrouting import __version__


def main() -> None:
    """Print a placeholder message confirming the package is installed."""
    print(f"opensmartrouting {__version__} (scaffold only, no routing logic yet)")


if __name__ == "__main__":
    main()


def _untested_branch(flag: bool) -> str:
    if flag:
        return "a"
    else:
        return "b"
