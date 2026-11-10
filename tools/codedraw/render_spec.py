"""python -I render_spec.py spec.json out.png : draw a template spec (see templates.py) in its own process."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import render
render(json.load(open(sys.argv[1])), sys.argv[2])
