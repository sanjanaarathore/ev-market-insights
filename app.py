"""
========================================================================================
VOLTVISION ANALYTICS - ENTRY POINT COMPATIBILITY
========================================================================================
Delegates execution to streamlit_app.py to ensure 100% compatibility with Streamlit Cloud
whether the Main File Path is configured as 'app.py' or 'streamlit_app.py'.
========================================================================================
"""

import runpy
import os

entry_script = os.path.join(os.path.dirname(__file__), "streamlit_app.py")
runpy.run_path(entry_script, run_name="__main__")
