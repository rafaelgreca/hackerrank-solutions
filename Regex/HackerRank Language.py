import re
import sys

n = int(sys.stdin.readline())
languages = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'.split(':')

for _ in range(n):
    string = sys.stdin.readline()
    
    language_detected = re.findall(r'[A-Z]+$', string)
    if language_detected[0] in languages:
        sys.stdout.write('VALID\n')
    else:
        sys.stdout.write('INVALID\n')