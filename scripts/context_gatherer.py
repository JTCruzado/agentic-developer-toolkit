# scripts/context_gatherer.py
import typer
from pathlib import Path

app = typer.Typer()

@app.command()
def gather(
    target_file: Path = typer.Argument(..., help="The path to the main Python file."),
    claude_format: bool = typer.Option(True, "--claude/--no-claude", help="Format output with XML tags for Claude.")
):
    """
Gathers the content of a target file and its corresponding test file,
then prints the combined context to the console.

Args:
    target_file (Path): The path to the main Python file.
    claude_format (bool): Flag to format output with XML tags for Claude.

Raises:
    typer.Exit: If the target file is not found or cannot be read.
    """
    if not target_file.is_file():
        typer.echo(f"Error: File not found at {target_file}", err=True)
        raise typer.Exit(code=1)

    main_content = target_file.read_text()
    typer.echo(f"✅ Successfully read {target_file}")

    # --- FIX: Improved Test File Discovery Logic ---
    test_file_name = f"test_{target_file.name}"
    
    # Let's check two common locations for the test file
    # Location 1: In a parallel 'tests' directory (e.g., sample_code/tests/test_utils.py)
    test_path_in_subdir = target_file.parent / "tests" / test_file_name
    # Location 2: Right next to the original file (e.g., sample_code/test_utils.py)
    test_path_alongside = target_file.parent / test_file_name
    
    test_content = ""
    test_file_path = None # To store the path of the found test file

    if test_path_in_subdir.is_file():
        test_file_path = test_path_in_subdir
    elif test_path_alongside.is_file():
        test_file_path = test_path_alongside

    if test_file_path:
        test_content = test_file_path.read_text()
        typer.echo(f"✅ Found and read test file at {test_file_path}")
    else:
        typer.echo(f"⚠️ Could not find a corresponding test file.")
    # --- END FIX ---

    typer.echo("\n--- Combined Context ---\n")
    if claude_format:
        print(f'<source_file path="{target_file}">\n{main_content}\n</source_file>')
        if test_content and test_file_path:
            print(f'\n<test_file path="{test_file_path}">\n{test_content}\n</test_file>')
    else:
        print(main_content)
        if test_content:
            print("\n--- Test File ---\n")
            print(test_content)

if __name__ == "__main__":
    app()