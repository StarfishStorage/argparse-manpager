from waflib.Task import Task
from waflib.TaskGen import feature
from waflib.Utils import O755, subst_vars, to_list

def options(ctx):
    ctx.load('python')

def configure(ctx):
    ctx.load('python')
    ctx.check_python_module('manpager')

class entrypynt(Task):
    vars = ["PYTHON", "MODULE"]

    def run(self):
        starter = self.outputs[0]
        starter.write("#!/bin/sh\n" +
                subst_vars("exec ${PYTHON} -m ${MODULE} $@", self.env))
        starter.chmod(O755)

@feature('entrypynt')
def generate_python_starter(self):
    for module, target in zip(to_list(self.modules),
            map(self.path.find_or_declare, to_list(self.target))):
        env = self.env.derive()
        env.MODULE = module
        self.create_task('entrypynt', tgt = target.change_ext('.sh'), env = env)