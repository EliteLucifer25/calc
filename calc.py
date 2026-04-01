#!/usr/bin/env python3
import sys
import argparse
import math

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass

class Calculator:
    def __init__(self):
        self.history = []
        
        # Build a safe dictionary of mathematical functions and constants
        self.safe_env = {
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
        }
        
        # Add all math module functions (except dunder methods and dangerous ones)
        for name in dir(math):
            if not name.startswith("_"):
                self.safe_env[name] = getattr(math, name)
                
        # Aliases for convenience
        self.safe_env["ln"] = math.log

    def evaluate(self, expression: str):
        """Safely evaluates a mathematical string expression."""
        if not expression or not expression.strip():
            return None
            
        # Provide previous results via '_' or 'ans'
        ans = self.history[-1] if self.history else 0
        self.safe_env["_"] = ans
        self.safe_env["ans"] = ans
        
        try:
            # Safely compile the expression first
            code = compile(expression, "<string>", "eval")
            
            # Check for invalid operations in the compiled AST before running eval
            for name in code.co_names:
                if name not in self.safe_env:
                    raise CalculatorError(f"Unsupported function or variable: '{name}'")
                    
            # Evaluate using an empty locals dictionary and our restricted globals
            result = eval(code, {"__builtins__": {}}, self.safe_env)
            
            # Store result in history
            self.history.append(result)
            return result
            
        except SyntaxError:
            raise CalculatorError("Invalid syntax in mathematical expression.")
        except ZeroDivisionError:
            raise CalculatorError("Division by zero is not allowed.")
        except OverflowError:
            raise CalculatorError("Math overflow: Number exceeds representation.")
        except TypeError as e:
            raise CalculatorError(f"Type error: {str(e)}")
        except NameError as e:
            raise CalculatorError(f"Name error: {str(e)}")
        except Exception as e:
            raise CalculatorError(f"Evaluation failed: {str(e)}")


def interactive_mode():
    """Starts the REPL session for the calculator."""
    print("="*50)
    print(" Advanced Python Calculator (Mathematical REPL)")
    print(" Type 'help' for functions, 'history' for past results.")
    print(" Use '_' or 'ans' to refer to the last result.")
    print(" Type 'quit' or 'exit' to close.")
    print("="*50)
    
    calc = Calculator()
    
    while True:
        try:
            expr = input("\ncalc> ").strip()
            
            if expr.lower() in ("exit", "quit", "q"):
                print("Goodbye!")
                break
            elif expr.lower() == "help":
                print("\nAvailable functions/constants:")
                funcs = [k for k in calc.safe_env.keys() if k not in ("_", "ans")]
                funcs.sort()
                print(", ".join(funcs))
                continue
            elif expr.lower() == "history":
                if not calc.history:
                    print("History is empty.")
                for i, res in enumerate(calc.history):
                    print(f"[{i+1}]: {res}")
                continue
            elif not expr:
                continue
                
            result = calc.evaluate(expr)
            if result is not None:
                # Format integer results neatly
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                print(f"= {result}")
                
        except CalculatorError as ce:
            print(f"Error: {ce}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def main():
    parser = argparse.ArgumentParser(
        description="An Advanced Terminal Calculator.",
        epilog="Examples:\n  python calc.py '5 + 5 * 2'\n  python calc.py 'sin(pi/2)'",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "expression", 
        nargs="?", 
        help="Mathematical expression to evaluate (quotes recommended)"
    )
    
    args = parser.parse_args()
    
    if args.expression:
        calc = Calculator()
        try:
            res = calc.evaluate(args.expression)
            if isinstance(res, float) and res.is_integer():
                res = int(res)
            print(res)
        except CalculatorError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # If no expression provided, start REPL
        interactive_mode()

if __name__ == "__main__":
    main()