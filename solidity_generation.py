def generate_smart_contract(token_name, token_symbol, total_supply):
    contract_template = f"""
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    contract {token_name} {{
        string public name = "{token_name}";
        string public symbol = "{token_symbol}";
        uint256 public totalSupply = {total_supply};

        mapping(address => uint256) public balances;

        constructor() {{
            balances[msg.sender] = totalSupply;
        }}

        function transfer(address to, uint256 amount) public returns (bool) {{
            require(balances[msg.sender] >= amount, "Not enough tokens");
            balances[msg.sender] -= amount;
            balances[to] += amount;
            return true;
        }}
    }}
    """
    return contract_template
