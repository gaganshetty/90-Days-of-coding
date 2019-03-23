#regex
import re


def validate_update_form(text):
    text_pattern = r"^[A-Za-z\s\d._!@#%&-+]+$"
    if re.search(text_pattern, text):
        print("Valid")
        return True
    else:
    	print("not valid")
    	return False


validate_update_form("<script>")