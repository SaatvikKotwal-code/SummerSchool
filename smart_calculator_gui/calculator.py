import re
import math

def smart_calculate(user_input):
    text = user_input.lower()

    text = text.replace("plus", "+").replace("add", "+")
    text = text.replace("minus", "-").replace("subtract", "-")
    text = text.replace("times", "*").replace("multiply", "*")
    text = text.replace("divided by", "/").replace("divide", "/")
    text = text.replace("percent of", "* 0.01 *")
    text = text.replace("percent", "* 0.01")
    text = text.replace("square root of", "sqrt")

    if "sqrt" in text:
        match = re.search(r"sqrt\\s*([0-9.]+)", text)
        if match:
            num = float(match.group(1))
            return f"Result: {math.sqrt(num)}"

    try:
        result = eval(text)
        return f"Result: {result}"
    except Exception:
        return "❌ Sorry, I couldn't understand the calculation."
