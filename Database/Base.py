
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.inspection import inspect

@as_declarative()
class CustomBase:
    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

Base = CustomBase