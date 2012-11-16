from os.path import dirname

from django.conf import settings
from pipeline.compilers import SubProcessCompiler


class HandlebarsCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.hbs')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        command = "%s %s -f %s" % (
            settings.PIPELINE_HANDLEBARS_BINARY,
            infile,
            outfile
            )
        return self.execute_command(command, cwd=dirname(infile))

