import gradio as gr
from calc import Calculator, CalculatorError

# Instantiate the global calculator to maintain history
calc = Calculator()

def compute(expression):
    try:
        if not expression or not expression.strip():
            return "Output will appear here..."
            
        result = calc.evaluate(expression)
        
        # Format integer results neatly
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        return str(result)
        
    except CalculatorError as ce:
        return f"Error: {str(ce)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

# Define the Gradio Interface
interface = gr.Interface(
    fn=compute,
    inputs=gr.Textbox(
        label="Mathematical Expression", 
        placeholder="e.g. 5 + max(3, 7) * sqrt(144) + sin(pi/2)",
        lines=2
    ),
    outputs=gr.Textbox(label="Result"),
    title="Advanced Python Calculator",
    description=("A highly robust, safe mathematical engine supporting complex expressions, "
                 "operator precedence, constants (`pi`, `e`), and functions like `sin`, `log`, `sqrt`, `max`, `abs`. "
                 "Use `_` or `ans` to reference the last evaluated answer!")
)

if __name__ == "__main__":
    interface.launch()
