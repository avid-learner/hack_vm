# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:15:55 2018

@author: someone
"""

#%%

from jinja2 import Template
template = Template('Hello {{ name }}!')
template.render(name='John Doe')

#%%

def nextLabel(counter=[1]):
    counter[0] += 1
    return "label"+str(counter[0])

from jinja2 import Template, Environment, PackageLoader, select_autoescape, FileSystemLoader, meta, StrictUndefined
import jinja2
import logging
from jinja2 import Environment, Undefined
from jinja2.exceptions import UndefinedError
logging.basicConfig()
logger = logging.getLogger('logger')
LoggingUndefined = jinja2.make_logging_undefined(logger=logger,base=jinja2.Undefined)
env = Environment(
        loader= FileSystemLoader('templates')
        )
env.globals.update(nextLabel=nextLabel)
template = env.get_template('gt.template')
ast=env.parse(template)
#jinja2.meta.find_undeclared_variables(ast) == set([])
print(template.render(start = 2423))


#%%
a = set()
print(a)
a.add(2)
print(a)
#%%
from jinja2 import Environment, meta
env = Environment()
txt = "// D == stack[SP-1] \
// M == stack[SP-2] \
D=D-M; \
@{{ unique_label_1 }} \
D;JEQ\
// result is false \
D=0\
@{{unique_label_2}}\
0;JEQ\
({{unique_label_1}})\
// result is true\
D=-1\
({{unique_label_2}})\
@SP\
"
ast = env.parse(txt)
meta.find_undeclared_variables(ast)
#%%