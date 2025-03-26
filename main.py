import os
from sympy import sympify

WHOAMI = os.environ.get("WHOAMI")
POST_TEXT = os.environ.get("POST")
FROM = os.environ.get("FROM")
PROCESSED_POST = os.environ.get("PROCESSED_POST", "")

def evaluate_expression(expr):
    try:
        result = sympify(expr)
        decimal_result = result.evalf()
        return round(decimal_result, 2)
    except Exception as e:
        return 


def main():
    # print("WHOAMI:", WHOAMI)
    # print("POST_TEXT:", POST_TEXT)
    # print("FROM:", FROM)
    # print("PROCESSED_POST:", PROCESSED_POST)

    result = evaluate_expression(PROCESSED_POST)

    if result is None:
        print("🔥🧮🔥")
    else:
        print(result)    

if __name__ == "__main__":
    main()