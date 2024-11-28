import pytest
from .llm import LLMConnector

@pytest.mark.asyncio
async def test_ask_openai():
    print("\nTesting OpenAI API call...")
    connector = LLMConnector("your-openai-key")
    response = await connector.ask_openai("Hello, how are you?")
    print(f"OpenAI Response: {response}")
    assert isinstance(response, str)
    assert len(response) > 0