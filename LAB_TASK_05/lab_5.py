import click

@click.command()
@click.argument('operation', type=click.Choice(['add', 'subtract', 'multiply', 'divide'], case_sensitive=False))
@click.argument('num1', type=float)
@click.argument('num2', type=float)
def calculate(operation, num1, num2):
    """Perform basic arithmetic operations."""
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            click.echo("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    
    click.echo(f"The result of {operation}ing {num1} and {num2} is: {result}")

if __name__ == '__main__':
    calculate()
