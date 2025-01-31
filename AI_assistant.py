def fix_code_error(code_snippet):
    if "pragma solidity" not in code_snippet:
        return "Error: Missing Solidity version declaration"
    if "constructor" not in code_snippet:
        return "Warning: No constructor found"
    return "Code looks good"

# Example of use
code = """
contract Test {
    function test() public {}
}
"""
print(fix_code_error(code))
