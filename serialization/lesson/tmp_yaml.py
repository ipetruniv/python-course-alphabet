import sys
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

class MyYAML(YAML):
    def dump(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()


yaml = MyYAML()
print(yaml.dump(dict(a=1, b=2), sys.stdout))
