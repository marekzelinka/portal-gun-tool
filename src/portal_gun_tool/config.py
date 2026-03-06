__project_name__ = "portal-gun-tool"


def get_version() -> str:
    """Get version lazily when needed"""
    import importlib.metadata

    return importlib.metadata.version(__project_name__)
