from mcp.server.fastmcp import FastMCP
import pandas as pd


mcp = FastMCP("Expense MCP Server")


@mcp.tool()
def get_expenses():

    data = pd.read_csv(
        "data/expenses.csv"
    )

    return data.to_dict(
        orient="records"
    )


@mcp.tool()
def calculate_total():

    data = pd.read_csv(
        "data/expenses.csv"
    )

    total = data["amount"].sum()

    return {
        "total_expense": total
    }


if __name__ == "__main__":
    mcp.run()