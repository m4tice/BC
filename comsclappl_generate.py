"""
author: @guu8hc
"""

from ComSclAppl.comsclappl_generator import Generator

if __name__ == "__main__":
    FILE_NAME = "ecucvalues.py"
    generator = Generator(FILE_NAME)
    generator.generate()
