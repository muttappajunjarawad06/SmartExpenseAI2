import asyncio
from agents.main_agent import expense_analyzer


async def main():

    question = input("Enter your expense question: ")

    result = expense_analyzer(question)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())